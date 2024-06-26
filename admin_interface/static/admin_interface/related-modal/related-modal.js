/** global: django */

if (typeof(django) !== 'undefined' && typeof(django.jQuery) !== 'undefined') {
    (function($) {

        $(document).ready(function() {

            function dismissModal() {
                $.magnificPopup.close();
            }

            // create the function that will close the modal
            function dismissRelatedObjectModal() {
                dismissModal();
            }

            function dismissRelatedLookupModal(win, chosenId) {
                const windowRef = win;
                const windowName = windowRef.name;
                const widgetName = windowName.replace(/^(change|add|delete|lookup)_/, '');
                const widgetEl = $('#' + widgetName);
                const widgetVal = widgetEl.val();
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

            function updateURLParameter(url, key, value) {
                const urlPattern = /^https?:\/\//i;
                if (!urlPattern.test(url)) {
                    url = window.location.origin + url;
                }
                const urlObject = new URL(url);
                urlObject.searchParams.set(key, value);
                return urlObject.toString();
            }

            function presentRelatedObjectModal(e) {
                const linkEl = $(this);

                const href = (linkEl.attr('href') || '');
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
                const iframeName = linkEl.attr('id');
                let iframeSrc = href;

                if (e.data.lookup !== true) {
                    // browsers stop loading nested iframes having the same src url
                    // create a random parameter and append it to the src url to prevent it
                    // this workaround doesn't work with related lookup url
                    const iframeSrcRandom = String(Math.round(Math.random() * 999999));
                    iframeSrc = updateURLParameter(iframeSrc, '_modal', iframeSrcRandom);
                }

                // fix for django 1.7 TODO remove
                iframeSrc = updateURLParameter(iframeSrc, '_popup', '1');

                // build the iframe html
                const iframeHTML = '<iframe id="related-modal-iframe" name="' + iframeName + '" src="' + iframeSrc + '"></iframe>';
                const modalHTML = '<div class="related-modal-iframe-container">' + iframeHTML + '</div>';
                const modalEl = $(modalHTML);
                const iframeEl = modalEl.find('#related-modal-iframe');

                if (e.data.lookup === true) {
                    // set current window as iframe opener because
                    // the callback is called on the opener window
                    iframeEl.on('load', function() {
                        const iframeObj = $(this).get(0);
                        const iframeWindow = iframeObj.contentWindow;
                        iframeWindow.opener = window;
                    });
                }

                // the modal css class
                let iframeInternalModalClass = 'related-modal';

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
                const data = {
                    lookup: (lookup === true ? true : false)
                };
                // remove potential existing click event listener
                const el = $(selector);
                el.removeAttr('onclick');
                el.unbind('click');
                el.click(data, presentRelatedObjectModal);
                // listen the event on document for handling it on elements will be added to the DOM later
                $(document).on('click', selector, data, presentRelatedObjectModal);
            }

            // assign functions to global variables
            window.presentRelatedObjectModal = presentRelatedObjectModal;
            window.presentRelatedObjectModalOnClickOn = presentRelatedObjectModalOnClickOn;

            presentRelatedObjectModalOnClickOn('a.related-widget-wrapper-link');

            // raw_id_fields support
            presentRelatedObjectModalOnClickOn('a.related-lookup', true);

            // django-dynamic-raw-id support - #61
            // https://github.com/lincolnloop/django-dynamic-raw-id
            presentRelatedObjectModalOnClickOn('a.dynamic_raw_id-related-lookup', true);

            // show_change_link=True support
            presentRelatedObjectModalOnClickOn('a.inlinechangelink');

            // any link with _popup=1 parameter support
            presentRelatedObjectModalOnClickOn('a[href*="_popup=1"]');

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
