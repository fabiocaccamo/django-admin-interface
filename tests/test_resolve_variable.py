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
            '{% admin_interface_resolve_variable "myvar" as res %}{{ res }}',
            {"myvar": "hello"},
        )
        self.assertEqual(out, "hello")

    def test_returns_default_when_missing(self):
        out = self.render_template(
            '{% admin_interface_resolve_variable "missingvar" as res %}{{ res }}'
        )
        self.assertEqual(out, "")

    def test_returns_custom_default(self):
        out = self.render_template(
            '{% admin_interface_resolve_variable "missingvar" "def" as res %}{{ res }}'
        )
        self.assertEqual(out, "def")

    def test_dotted_variable_existing(self):
        context = {"user": {"name": "alice"}}
        out = self.render_template(
            '{% admin_interface_resolve_variable "user.name" as res %}{{ res }}',
            context,
        )
        self.assertEqual(out, "alice")

    def test_dotted_variable_missing_middle_key(self):
        context = {"user": {}}
        out = self.render_template(
            '{% admin_interface_resolve_variable "user.name" "def" as res %}{{ res }}',
            context,
        )
        self.assertEqual(out, "def")

    def test_dotted_variable_missing_top_key(self):
        out = self.render_template(
            '{% admin_interface_resolve_variable "user.name" "guest" as res %}{{ res }}'
        )
        self.assertEqual(out, "guest")

    def test_dotted_variable_with_object_attribute(self):
        class User:
            def __init__(self):
                self.name = "bob"

        context = {"user": User()}
        out = self.render_template(
            '{% admin_interface_resolve_variable "user.name" as res %}{{ res }}',
            context,
        )
        self.assertEqual(out, "bob")

    def test_dotted_variable_partial_attribute_missing(self):
        class User:
            pass

        context = {"user": User()}
        out = self.render_template(
            '{% admin_interface_resolve_variable "user.name"  as res %}{{ res }}',
            context,
        )
        self.assertEqual(out, "")

    def test_non_dict_non_object_root(self):
        context = {"user": "notadict"}
        out = self.render_template(
            '{% admin_interface_resolve_variable "user.name"  as res %}{{ res }}',
            context,
        )
        self.assertEqual(out, "")

    def test_dotted_variable_object_with_nested_dict(self):
        class User:
            def __init__(self):
                self.info = {"name": "bob"}

        context = {"user": User()}
        out = self.render_template(
            '{% admin_interface_resolve_variable "user.info.name" as res %}{{ res }}',
            context,
        )
        self.assertEqual(out, "bob")
