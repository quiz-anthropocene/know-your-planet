import requests
import json
from datetime import datetime, date

import notion  # https://github.com/jamalex/notion-py
from notion.client import NotionClient

from django.conf import settings
from django.db.models.fields import URLField

from api.models import Question


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"  # "2021-05-05T13:02:00.000Z"  # milliseconds not managed
QUESTION_URL_FIELDS = [field.name for field in Question._meta.fields if type(field) == URLField]


# Official API

def get_question_table_pages(start_cursor=None):
    """
    Retrive 100 pages from the question table
    """
    url = f"https://api.notion.com/v1/databases/{settings.NOTION_QUESTION_TABLE_ID}/query"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {settings.NOTION_API_SECRET}", "Notion-Version": f"{settings.NOTION_API_VERSION}"}
    data = {"sorts": [{"property": "Last edited time", "direction": "descending"}]}
    if start_cursor:
        data["start_cursor"] = start_cursor

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        raise Exception(json.loads(response._content))

    return response


def process_page_properties(page_properties):
    """
    # cleanup fields
    # - field type --> "" if None
    # - field difficulty to int
    # - field answer_correct --> "" if None
    # - field added --> created time if None --> to date
    # - field validator --> "" if None
    # - fields answer_explanation, answer_image_explanation & answer_extra_info --> clean markdown [links](links)  # noqa
    # - fields '_url' --> strip spaces at end (or else we get a ValidationError)
    if notion_question_dict["type"] is None:
        notion_question_dict["type"] = ""
    if notion_question_dict["language"] is None:
        notion_question_dict["language"] = ""
    if notion_question_dict["answer_correct"] is None:
        notion_question_dict["answer_correct"] = ""
    if notion_question_dict["validator"] is None:
        notion_question_dict["validator"] = ""
    # clean markdown [links](links)
    for field_name in ["answer_explanation", "answer_image_explanation", "answer_extra_info"]:
        if "http" in notion_question_dict[field_name]:
            notion_question_dict[field_name] = utilities.clean_markdown_links(
                notion_question_dict[field_name]
            )
    # strip spaces in url fields
    for field_name in QUESTION_URL_FIELDS:
        if field_name in notion_question_dict:
            notion_question_dict[field_name] = notion_question_dict[field_name].strip()

    return notion_question_dict
    """
    page_dict = dict()
    for key in page_properties:
        # Step 1: process key by Notion 'type"
        if page_properties[key]["type"] == "title":
            page_dict[key] = "".join([text["plain_text"] for text in page_properties[key]["title"]])
        elif page_properties[key]["type"] == "rich_text":
            page_dict[key] = "".join([text["plain_text"] for text in page_properties[key]["rich_text"]])
        elif page_properties[key]["type"] == "number":
            page_dict[key] = page_properties[key]["number"]
        elif page_properties[key]["type"] == "select":
            try:
                page_dict[key] = page_properties[key]["select"]["name"]
            except (TypeError, AttributeError) as e:
                page_dict[key] = ""
        elif page_properties[key]["type"] == "multi_select":
            page_dict[key] = [tag["name"] for tag in page_properties[key]["multi_select"]]
        elif page_properties[key]["type"] == "url":
            try:
                page_dict[key] = page_properties[key]["url"].strip()
            except (TypeError, AttributeError) as e:
                page_dict[key] = ""
        elif page_properties[key]["type"] == "checkbox":
            page_dict[key] = page_properties[key]["checkbox"]  # True or False
        elif page_properties[key]["type"] == "date":
            try:
                page_dict[key] = page_properties[key]["date"]["start"]
            except (TypeError, AttributeError) as e:
                page_dict[key] = ""
        elif page_properties[key]["type"] == "created_time":
            page_dict[key] = page_properties[key]["created_time"]
        elif page_properties[key]["type"] == "created_by":
            page_dict[key] = page_properties[key]["created_by"]
        elif page_properties[key]["type"] == "last_edited_by":
            page_dict[key] = page_properties[key]["last_edited_by"]
        elif page_properties[key]["type"] == "last_edited_time":
            page_dict[key] = page_properties[key]["last_edited_time"]
        else:
            raise Exception(f"process_page_properties: {page_properties[key]['type']} missing")
        
        # Step 2: process key by custom rules
        if key == "Text":
            page_dict["text"] = page_dict[key]
        if key == "difficulty":
            page_dict[key] = int(page_dict[key]) if page_dict[key] else None
        elif key == "added":
            page_dict[key] = date.fromisoformat(page_dict[key]) if page_dict[key] else datetime.strptime(page_dict["Created time"][:-5], TIMESTAMP_FORMAT).date()

    return page_dict


# Unofficial API (notion-py)

def get_notion_client():
    """
    Connection
    """
    # try:
    #     client = NotionClient(token_v2=settings.NOTION_TOKEN_V2)
    # except Exception as e:
    #     # usually: 401 Client Error: Unauthorized for url: https://www.notion.so/api/v3/loadUserContent # noqa
    #     print(e)
    #     raise
    client = NotionClient(token_v2=settings.NOTION_TOKEN_V2)
    return client


def get_questions_table():
    """
    Questions page: get table
    """
    notion_client = get_notion_client()
    # page = client.get_block(settings.NOTION_QUESTIONS_PAGE_URL)
    table = notion_client.get_collection_view(settings.NOTION_QUESTIONS_TABLE_URL)
    return table


def get_questions_table_rows():
    """
    Questions page: get current rows
    """
    questions_table = get_questions_table()
    rows = questions_table.collection.get_rows()
    return rows


def get_contribution_table():
    """
    Contribution page: get table
    """
    notion_client = get_notion_client()
    # page = client.get_block(settings.NOTION_CONTRIBUTION_PAGE_URL)
    table = notion_client.get_collection_view(settings.NOTION_CONTRIBUTION_TABLE_URL)
    return table


def add_contribution_row(
    contribution_text: str,
    contribution_description: str,
    contribution_type: str,
    contribution_date=datetime.now(),
):
    """
    Contribution page: add row
    """
    # init
    contribution_table = get_contribution_table()
    # add row
    row = contribution_table.collection.add_row()
    row.type = contribution_type
    row.text = contribution_text
    row.description = contribution_description
    # row.created = notion.collection.NotionDate(date.today())
    row.created = notion.collection.NotionDate(contribution_date)
    return row


def get_import_stats_table():
    """
    Import stats page: get table
    """
    notion_client = get_notion_client()
    # page = client.get_block(settings.NOTION_IMPORT_STATS_PAGE_URL)
    table = notion_client.get_collection_view(
        settings.NOTION_IMPORT_STATS_TABLE_URL + "coucou"
    )
    return table


def add_import_stats_row(total, new, update):
    """
    Import stats page: add row
    """
    # init
    import_stats_table = get_import_stats_table()
    # add row
    row = import_stats_table.collection.add_row()
    row.action = "import"
    row.question_total = total
    row.question_new = new
    row.question_update = update
    row.date = notion.collection.NotionDate(datetime.now())
    return row


def get_glossary_table():
    """
   Glossary page: get table
    """
    notion_client = get_notion_client()
    # page = client.get_block(settings.NOTION_GLOSSARY_PAGE_URL)
    table = notion_client.get_collection_view(settings.NOTION_GLOSSARY_TABLE_URL)
    return table


def get_glossary_rows():
    """
   Glossary page: get current rows
    """
    glossary_table = get_glossary_table()
    # sort_params = [{
    #     "property": "name",
    #     "direction": "descending",
    # }]
    # glossary_table_sorted = glossary_table.build_query(sort=sort_params).execute()
    rows = glossary_table.collection.get_rows()
    return rows
