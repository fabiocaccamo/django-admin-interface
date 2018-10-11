(function($) {
    'use strict';
    $(function() {
        $('.cancel-link').click(function(e) {
            e.preventDefault();
            var parentWindow = window.parent;
            if (parentWindow && typeof(parentWindow.dismissRelatedObjectModal) === 'function') {
                parentWindow.dismissRelatedObjectModal();
            } else {
                // fallback to default behavior
                history.back();
            }
            return false;
        });
    });
})(django.jQuery);