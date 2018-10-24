(function() {

    'use strict';

    function getModalWindowData()
    {
        var windowRef = window;
        var windowName = windowRef.name;
        var widgetName = windowName.replace(/^(change|add|delete|lookup)_/, '');
        var modalRef = {};
        var openerRef = windowRef.opener;
        if (!openerRef) {
            openerRef = windowRef.parent;
            modalRef = {
                name: openerRef.id_to_windowname(widgetName),
                close: function(){
                    openerRef.dismissRelatedObjectModal();
                }
            };
        }
        return { opener:openerRef, modal:modalRef };
    }

    var modalData = getModalWindowData();
    var modalRef = modalData['modal'];
    var openerRef = modalData['opener'];

    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    // console.log(initData);
    switch (initData.action) {
        case 'change':
            if (typeof(openerRef.dismissChangeRelatedObjectPopup) === 'function') {
                openerRef.dismissChangeRelatedObjectPopup(modalRef, initData.value, initData.obj, initData.new_value);
            }
            break;
        case 'delete':
            if (typeof(openerRef.dismissDeleteRelatedObjectPopup) === 'function') {
                openerRef.dismissDeleteRelatedObjectPopup(modalRef, initData.value);
            }
            break;
        default:
            if (typeof(openerRef.dismissAddRelatedObjectPopup) === 'function') {
                openerRef.dismissAddRelatedObjectPopup(modalRef, initData.value, initData.obj);
            }
            else if (typeof(openerRef.dismissAddAnotherPopup) === 'function') {
                // django 1.7 compatibility
                openerRef.dismissAddAnotherPopup(modalRef, initData.value, initData.obj);
            }
            break;
    }

})();