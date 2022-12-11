(function() {

    'use strict';

    var windowRef = window;
    var openerRef = windowRef.parent;

    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch (initData.action) {
        case 'change':
            openerRef.streamapps[initData.app_id].updateBlock(initData.block_id, initData.instance_id);
            openerRef.dismissRelatedObjectModal();
            break;
        case 'delete':
            break;
        default:
            openerRef.streamapps[initData.app_id].updateBlock(initData.block_id, initData.instance_id);
            openerRef.dismissRelatedObjectModal();
            break;
    }

})();
