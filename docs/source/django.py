import inspect
import os

from django.core.wsgi import get_wsgi_application
from django.db import models
from django.utils.encoding import force_str
from django.utils.html import strip_tags

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuickStartAPI.settings")
get_wsgi_application()


def process_docstring(app, what, name, klass, options, lines):  # noqa: WPS211
    """Causes import errors if left outside the function."""  # noqa: DAR101, DAR201, E501
    # Only look at objects that inherit from Django's base model class
    if inspect.isclass(klass) and issubclass(klass, models.Model):
        # Grab the field list from the meta class
        fields = klass._meta.fields  # noqa: WPS437

        for field in fields:
            # Decode and strip any html out of the field's help text
            help_text = strip_tags(force_str(field.help_text))

            # Decode and capitalize the verbose name, for use if there isn't
            # any help text
            verbose_name = force_str(field.verbose_name).capitalize()

            if help_text:
                # Add the model field to the end of the docstring as a param
                # using the help text as the description
                lines.append(
                    ":param {0}: {1}".format(field.attname, help_text),
                )
            else:
                # Add the model field to the end of the docstring as a param
                # using the verbose name as the description
                lines.append(
                    ":param {0}: {1}".format(field.attname, verbose_name),
                )

            # Add the field's type to the docstring
            lines.append(
                ":type {0}: {1}".format(field.attname, type(field).__name__),
            )

    # Return the extended docstring
    return lines


def setup(app):
    """Register the docstring processor with sphinx."""  # noqa: DAR101
    app.connect("autodoc-process-docstring", process_docstring)
