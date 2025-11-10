(function() {
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.language-chooser form.language-chooser-select-form select').forEach(select => {
            select.addEventListener('change', () => {
                select.form.submit();
            });
        });
    });
})();
