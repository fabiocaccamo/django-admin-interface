(function() {
    // document.currentScript is only defined while the script is being parsed
    const script = document.currentScript;
    const envColor = script?.dataset?.envColor;

    if (envColor && envColor !== '') {
        document.addEventListener('DOMContentLoaded', () => {
            const favicon = new Favico({
                type: 'circle',
                bgColor: envColor,
                textColor: '#FFFFFF',
                animation: 'none'
            });
            favicon.badge(' ');
        });
    }
})();
