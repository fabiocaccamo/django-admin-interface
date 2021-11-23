(function() {
    window.onload = function() {
        for (let moduleEl of document.querySelectorAll('.admin-interface.foldable-apps [class^="app-"].module')) {
            // apply collapsed value from localstorage value
            let moduleAppClass = null;
            let moduleCollapsedClass = 'collapsed';
            moduleEl.classList.forEach(function(className) {
                if (className.startsWith('app-')) {
                    moduleAppClass = className;
                }
            });
            if (moduleAppClass) {
                let moduleAppKey = 'admin-interface.foldable-apps_' + moduleAppClass + '_collapsed';
                let moduleCollapsed = Boolean(parseInt((localStorage.getItem(moduleAppKey) || 0)) || 0);
                if (moduleCollapsed === true) {
                    moduleEl.classList.add(moduleCollapsedClass);
                } else {
                    moduleEl.classList.remove(moduleCollapsedClass);
                }
                // attach click for togggle collapsed class
                for (let captionEl of moduleEl.querySelectorAll('caption')) {
                    captionEl.onclick = function(event) {
                        // only when not clicking on the app name link
                        if (event.target.tagName.toLowerCase() === 'caption') {
                            moduleEl.classList.toggle(moduleCollapsedClass);
                            moduleCollapsed = moduleEl.classList.contains(moduleCollapsedClass);
                            localStorage.setItem(moduleAppKey, (moduleCollapsed ? 1 : 0));
                        }
                    };
                }
            }
            moduleEl.classList.add('foldable-apps-ready');
        }
    };
})();