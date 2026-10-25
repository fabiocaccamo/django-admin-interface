(function() {
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.list-filter-dropdown select').forEach(select => {
            select.addEventListener('change', (event) => {
                const value = event.target.value;
                if (!value) {
                    return;
                }

                try {
                    const url = new URL(value, window.location.href);
                    if (
                        (url.protocol === 'http:' || url.protocol === 'https:') &&
                        url.origin === window.location.origin
                    ) {
                        window.location = url.href;
                    }
                } catch (error) {
                    // Ignore invalid URLs.
                }
            });
        });
    });
})();
