/** global: django */

if (typeof(django) !== 'undefined' && typeof(django.jQuery) !== 'undefined')
{
    (function($) {

        $(document).ready(function(){

            function dismissModal()
            {
                $.magnificPopup.close();
            }

            // create the function that will close the modal
            function dismissRelatedObjectModal()
            {
                dismissModal();
            }

            function dismissRelatedLookupModal(win, chosenId)
            {
                var windowRef = win;
                var windowName = windowRef.name;
                var widgetName = windowName.replace(/^(change|add|delete|lookup)_/, '');
                var widgetEl = $('#' + widgetName);
                var widgetVal = widgetEl.val();
                if (widgetEl.hasClass('vManyToManyRawIdAdminField') && Boolean(widgetVal)) {
                    widgetEl.val(widgetVal + ', ' + chosenId);
                } else {
                    widgetEl.val(chosenId);
                }
                dismissModal();
            }

            // assign functions to global variables
            window.dismissRelatedObjectModal = dismissRelatedObjectModal;
            window.dismissRelatedLookupPopup = dismissRelatedLookupModal;

            function presentRelatedObjectModal(e)
            {
                var linkEl = $(this);

                var href = (linkEl.attr('href') || '');
                if (href === '') {
                    return;
                }

                // open the popup as modal
                e.preventDefault();
                e.stopImmediatePropagation();

                // remove focus from clicked link
                linkEl.blur();

                // use the clicked link id as iframe name
                // it will be available as window.name in the loaded iframe
                var iframeName = linkEl.attr('id');
                var iframeSrc = href;

                if (e.data.lookup !== true)
                {
                    // browsers stop loading nested iframes having the same src url
                    // create a random parameter and append it to the src url to prevent it
                    // this workaround doesn't work with related lookup url
                    var iframeSrcRandom = String(Math.round(Math.random() * 999999));
                    if (iframeSrc.indexOf('?') === -1) {
                        iframeSrc += '?_modal=' + iframeSrcRandom;
                    } else {
                        iframeSrc += '&_modal=' + iframeSrcRandom;
                    }
                }

                // fix for django 1.7
                if (iframeSrc.indexOf('_popup=1') === -1) {
                    if (iframeSrc.indexOf('?') === -1) {
                        iframeSrc += '?_popup=1';
                    } else {
                        iframeSrc += '&_popup=1';
                    }
                }

                // build the iframe html
                var iframeHTML = '<iframe id="related-modal-iframe" name="' + iframeName + '" src="' + iframeSrc + '"></iframe>';
                var modalHTML = '<div class="related-modal-iframe-container">' + iframeHTML + '</div>';
                var modalEl = $(modalHTML);
                var iframeEl = modalEl.find('#related-modal-iframe');

                if (e.data.lookup === true)
                {
                    // set current window as iframe opener because
                    // the callback is called on the opener window
                    iframeEl.on('load', function() {
                        var iframeObj = $(this).get(0);
                        var iframeWindow = iframeObj.contentWindow;
                        iframeWindow.opener = window;
                    });
                }

                // the modal css class
                var iframeInternalModalClass = 'related-modal';

                // if the current window is inside an iframe, it means that it is already in a modal,
                // append an additional css class to the modal to offer more customization
                if (window.top !== window.self) {
                    iframeInternalModalClass += ' related-modal__nested';
                }

                // open the popup using magnific popup
                $.magnificPopup.open({
                    mainClass: iframeInternalModalClass,
                    fixedContentPos: false,
                    showCloseBtn: true,
                    closeBtnInside: true,
                    items: {
                        src: modalEl,
                        type: 'inline'
                    }
                });

                return false;
            }

            // listen click events on related links
            function presentRelatedObjectModalOnClickOn(selector, lookup) {
                var data = {
                    lookup:(lookup === true ? true : false)
                };
                var el = $(selector);
                el.removeAttr('onclick');
                el.unbind('click');
                el.click(data, presentRelatedObjectModal);
            }

            // assign functions to global variables
            window.presentRelatedObjectModal = presentRelatedObjectModal;
            window.presentRelatedObjectModalOnClickOn = presentRelatedObjectModalOnClickOn;

            // django 1.7 compatibility
            presentRelatedObjectModalOnClickOn('a.add-another');

            // django 1.8 and above
            presentRelatedObjectModalOnClickOn('a.related-widget-wrapper-link');

            // raw_id_fields support
            presentRelatedObjectModalOnClickOn('a.related-lookup', true);

            // django-dynamic-raw-id support - #61
            // https://github.com/lincolnloop/django-dynamic-raw-id
            presentRelatedObjectModalOnClickOn('a.dynamic_raw_id-related-lookup', true);

            // django-streamfield support
            // https://github.com/raagin/django-streamfield/
            presentRelatedObjectModalOnClickOn('.streamfield_app a.stream-btn[href*="_popup=1"]');
            // Vanilla js for catching the click during capture phase for anticipating Vue.js listener.
            document.addEventListener('click', function(event) {
                // console.log('click intercepted before Vue.');
                if (event.target.matches('.streamfield_app a.stream-btn[href*="_popup=1"]')) {
                    event.stopImmediatePropagation();
                    event.preventDefault();
                    $(event.target).trigger('click');
                }
            }, { capture: true });
        });

    })(django.jQuery);
}
