if(typeof django !== 'undefined' && typeof django.jQuery !== 'undefined' )
{
    (function($) {

        $(document).ready(function(){

            // create the function that will close the modal
            function dismissRelatedObjectModal()
            {
                // close the popup as modal
                $.magnificPopup.close();
            }

            // assign the function to a global variable
            window.dismissRelatedObjectModal = dismissRelatedObjectModal;

            function presentRelatedObjectModal(e)
            {
                var href = ($(this).attr('href') || '');
                if( href == '' ){
                    return;
                }

                // open the popup as modal
                e.preventDefault();
                e.stopImmediatePropagation();

                // remove focus from clicked link
                $(this).blur();

                // use the clicked link id as iframe name
                // it will be available as window.name in the loaded iframe
                var iframeName = $(this).attr('id');
                // var iframeName = String(window.name + '____' + $(this).attr('id'));
                // console.log('open modal with name: "' + iframeName + '"');

                // browsers stop loading nested iframes having the same src url
                // create a random parameter and append it to the src url to prevent it
                var iframeSrcRandom = String(Math.round(Math.random() * 999999));
                var iframeSrc = href;

                // fix for django 1.7
                if( iframeSrc.indexOf('_popup=1') == -1 ){
                    iframeSrc += '&_popup=1';
                }

                iframeSrc += '&_modal=' + iframeSrcRandom;

                // build the iframe html
                // var iframeHTML = '<iframe id="related-modal" name="' + iframeName + '" src="' + iframeSrc + '"></iframe>';
                var iframeHTML = '<iframe id="related-modal-iframe" name="' + iframeName + '" src="' + iframeSrc + '"></iframe>';

                // create the iframe jquery element
                var iframeEl = $(iframeHTML);

                // the modal css class
                var iframeInternalModalClass = 'related-modal';

                // if the current window is inside an iframe, it means that it is already in a modal,
                // append an additional css class to the modal to offer more customization
                if( window.top != window.self )
                {
                    iframeInternalModalClass += ' related-modal__nested';
                }

                // open the popup using magnific popup
                $.magnificPopup.open({
                    mainClass: iframeInternalModalClass,
                    items: {
                        src: iframeEl,
                        type: 'inline'
                    }
                });

                return false;
            }

            // listen click events on related links

            // django 1.7 compatibility
            $('a.add-another').removeAttr('onclick');
            $('a.add-another').click( presentRelatedObjectModal );

            // django 1.8 and above
            $('a.related-widget-wrapper-link').click( presentRelatedObjectModal );
        });

    })(django.jQuery);
}

