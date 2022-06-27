from pathlib import Path
from typing import Mapping
from jinja2 import Environment, FileSystemLoader, select_autoescape


def generate_html(template_path: Path, target_path: Path, context: Mapping) -> None:
    """Generate HTML file from jinja2 template and context variables

    :param template_path: Full path to a jinja2 template
    :param target_path: Destination for generated file
    :param context: A dictionary of variables for the template generation
    """
    env = Environment(
        loader=FileSystemLoader(template_path.parent), autoescape=select_autoescape
    )
    template = env.get_template(template_path.name)
    with open(target_path, "w") as fh:
        fh.write(template.render(**context))
