document.addEventListener('DOMContentLoaded', function() {
    /**
     * Multiselect dropdown for the tag search form field
     */

    const tagFormElement = document.querySelector('#id_tags');
    const tagFormPlaceholder = 'Choisir 1 ou plusieurs tags';

    const buttonTextAndTitle = function(options, select) {
        if (options.length === 0) {
            return tagFormPlaceholder;
        }
        else if (options.length > 4) {
            return `${options.length} tags sélectionnés`;
        }
        else {
            var labels = [];
            options.each(function() {
                if ($(this).attr('label') !== undefined) {
                    labels.push($(this).attr('label'));
                }
                else {
                    labels.push($(this).html());
                }
            });
            return labels.join(', ') + '';
        }
    }

    // only on pages with id_tags
    if (document.body.contains(tagFormElement)) {
        $('#id_tags').multiselect({
            // height & width
            maxHeight: 400,
            buttonWidth: '100%',
            widthSynchronizationMode: 'always',
            // button
            buttonTextAlignment: 'left',
            buttonText: buttonTextAndTitle,
            buttonTitle: buttonTextAndTitle,
            // filter options
            enableFiltering: true,
            enableCaseInsensitiveFiltering: true,
            filterPlaceholder: tagFormPlaceholder,
            // reset button
            includeResetOption: true,
            includeResetDivider: true,
            resetText: 'Réinitialiser la sélection',
            // enableResetButton: true,
            // resetButtonText: 'Réinitialiser',
            // ability to select all group's child options in 1 click
            enableClickableOptGroups: true,
            // other
            buttonContainer: '<div id="id_tag_multiselect" class="btn-group" />',
            widthSynchronizationMode: 'ifPopupIsSmaller',
            // enableHTML: true,
            // nonSelectedText: `<span class="text-muted">${tagFormPlaceholder}</span>`,
            templates: {
                // fix for Bootstrap5: https://github.com/davidstutz/bootstrap-multiselect/issues/1226
                button: '<button type="button" class="form-select multiselect dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"><span class="multiselect-selected-text"></span></button>'
            },
        });

        // hack to set the placeholder color to grey when there is no item selected
        const multiselectSelectedText = document.querySelector('#id_tag_multiselect .multiselect-selected-text');
        if (multiselectSelectedText.innerText === tagFormPlaceholder) {
            multiselectSelectedText.classList.add('text-muted');
        }
        multiselectSelectedText.addEventListener('DOMSubtreeModified', function () {
            if (this.innerText === tagFormPlaceholder) {
                this.classList.add('text-muted');
            } else {
                this.classList.remove('text-muted');
            }
        })
    }

});