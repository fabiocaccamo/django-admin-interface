from django.template import Context, Template
from django.test import SimpleTestCase


class ResolveVariableTagTests(SimpleTestCase):
    def render_template(self, tpl, context=None):
        if context is None:
            context = {}
        return (
            Template("{% load admin_interface_tags %}" + tpl)
            .render(Context(context))
            .strip()
        )

    def test_returns_existing_variable(self):
        out = self.render_template(
            '{% resolve_variable "myvar" as result %}{{ result }}', {"myvar": "hello"}
        )
        self.assertEqual(out, "hello")

    def test_returns_default_when_missing(self):
        out = self.render_template(
            '{% resolve_variable "missingvar" as result %}{{ result }}'
        )
        self.assertEqual(out, "")

    def test_returns_custom_default(self):
        out = self.render_template(
            '{% resolve_variable "missingvar" "fallback" as result %}{{ result }}'
        )
        self.assertEqual(out, "fallback")
