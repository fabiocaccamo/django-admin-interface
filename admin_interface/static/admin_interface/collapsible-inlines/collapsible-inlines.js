/** global: django */

if (typeof(django) !== 'undefined' && typeof(django.jQuery) !== 'undefined')
{
    (function($) {

        $(document).ready(function(){

            function collapsibleInline(scope, collapsed) {
                var fieldsetCollapsed = collapsed;
                var fieldsetEl = $(scope).find('> fieldset.module');
                fieldsetEl.addClass('collapse');
                var fieldsetHasErrors = (fieldsetEl.children('.errors').length > 0);
                if (fieldsetHasErrors === true) {
                    fieldsetCollapsed = false;
                }
                if (fieldsetCollapsed === true) {
                    fieldsetEl.addClass('collapsed');
                }
                var collapseToggleText = (fieldsetCollapsed ? gettext('Show') : gettext('Hide'));
                var collapseToggleHTML = ' (<a class="collapse-toggle" href="#">' + collapseToggleText + '</a>)';
                var headerEl = fieldsetEl.find('> h2,> h3');
                headerEl.append(collapseToggleHTML);
            }

            var stackedInlinesOptionSel = '.admin-interface.collapsible-stacked-inlines';
            var stackedInlinesSel = stackedInlinesOptionSel + ' .inline-group[data-inline-type="stacked"]';
            var stackedInlinesCollapsed = $(stackedInlinesOptionSel).hasClass('collapsible-stacked-inlines-collapsed');

            var tabularInlinesOptionSel = '.admin-interface.collapsible-tabular-inlines';
            var tabularInlinesSel = tabularInlinesOptionSel + ' .inline-group[data-inline-type="tabular"] .inline-related.tabular';
            var tabularInlinesCollapsed = $(stackedInlinesOptionSel).hasClass('collapsible-tabular-inlines-collapsed');

            $(stackedInlinesSel).each(function() {
                collapsibleInline(this, stackedInlinesCollapsed);
            });

            $(tabularInlinesSel).each(function() {
                collapsibleInline(this, tabularInlinesCollapsed);
            });

        });

    })(django.jQuery);
}
