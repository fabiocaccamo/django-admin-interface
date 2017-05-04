if(typeof django !== 'undefined' && typeof django.jQuery !== 'undefined' )
{
    (function($) {

        $(document).ready(function(){

            // create the function that will close the modal
            function dismissRelatedObjectModal()
            {
                // close the popup
                $.magnificPopup.close();
            }

            // assign the function to a global variable
            window.dismissRelatedObjectModal = dismissRelatedObjectModal;

            // listen click events on related links
            // (:link prevents to listen click event if href is not defined)
            $('a.related-widget-wrapper-link:link').click(function(e){

                e.preventDefault();

                // remove focus from clicked link
                $(this).blur();

                // use the clicked link id as iframe name
                // it will be available as window.name in the loaded iframe
                var iframeName = $(this).attr('id');
                //var iframeName = String(window.name + '____' + $(this).attr('id'));
                //console.log('open modal with name: "' + iframeName + '"');

                // browsers stop loading nested iframes having the same src url
                // create a random parameter and append it to the src url to prevent it
                var iframeSrcRandom = String(Math.round(Math.random() * 999999));
                var iframeSrc = $(this).attr('href') + '&_modal=' + iframeSrcRandom;

                // build the iframe html
                //var iframeHTML = '<iframe id="related-modal" name="' + iframeName + '" src="' + iframeSrc + '"></iframe>';
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
            });
        });

    })(django.jQuery);
}

