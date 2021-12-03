(function() {

    'use strict';

    var windowRef = window;
    var windowName, widgetName;
    var openerRef = windowRef.opener;
    if (!openerRef) {
        // related modal is active
        openerRef = windowRef.parent;
        windowName = windowRef.name;
        widgetName = windowName.replace(/^(change|add|delete|lookup)_/, '');
        if (typeof(openerRef.id_to_windowname) === 'function') {
            // django < 3.1 compatibility
            widgetName = openerRef.id_to_windowname(widgetName);
        }
        windowRef = {
            name: widgetName,
            close: function() {
                openerRef.dismissRelatedObjectModal();
            }
        };
    }

    // default django popup_response.js
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch (initData.action) {
        case 'change':
            if (typeof(openerRef.dismissChangeRelatedObjectPopup) === 'function') {
                openerRef.dismissChangeRelatedObjectPopup(windowRef, initData.value, initData.obj, initData.new_value);
            }
            break;
        case 'delete':
            if (typeof(openerRef.dismissDeleteRelatedObjectPopup) === 'function') {
                openerRef.dismissDeleteRelatedObjectPopup(windowRef, initData.value);
            }
            break;
        default:
            if (typeof(openerRef.dismissAddRelatedObjectPopup) === 'function') {
                openerRef.dismissAddRelatedObjectPopup(windowRef, initData.value, initData.obj);
            }
            else if (typeof(openerRef.dismissAddAnotherPopup) === 'function') {
                // django 1.7 compatibility
                openerRef.dismissAddAnotherPopup(windowRef, initData.value, initData.obj);
            }
            break;
    }

})();