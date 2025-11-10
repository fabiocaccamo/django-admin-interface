(function() {
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.list-filter-dropdown select').forEach(select => {
            select.addEventListener('change', (event) => {
                const value = event.target.value;
                if (value) {
                    window.location = value;
                }
            });
        });
    });
})();
