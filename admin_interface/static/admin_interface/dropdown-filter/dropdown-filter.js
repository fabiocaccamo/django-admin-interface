(function() {
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.list-filter-dropdown select').forEach(select => {
            select.addEventListener('change', (event) => {
                const value = event.target.value;
                if (value && (value.startsWith('?') || (value.startsWith('/') && !value.startsWith('//')))) {
                    window.location = value;
                }
            });
        });
    });
})();
