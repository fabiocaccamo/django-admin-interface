/** global: django */

if (typeof(django) !== 'undefined' && typeof(django.jQuery) !== 'undefined') {
    (function($) {
        'use strict';
        $(document).ready(function() {
            $('.cancel-link').click(function(e) {
                e.preventDefault();
                var parentWindow = window.parent;
                if (parentWindow && typeof(parentWindow.dismissRelatedObjectModal) === 'function' && parentWindow !== window) {
                    parentWindow.dismissRelatedObjectModal();
                } else {
                    // fallback to default behavior
                    window.history.back();
                }
                return false;
            });
        });
    })(django.jQuery);
}