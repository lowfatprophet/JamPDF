import importlib.resources
import os
from typing import Any

import jinja2


def template_env() -> jinja2.Environment:
    return jinja2.Environment(
        # loader=jinja2.PackageLoader(package_name="jampdf",
        # package_path="_templates"),
        loader=jinja2.FileSystemLoader("_templates"),
        autoescape=jinja2.select_autoescape(),
    )


def get_default_template(env: jinja2.Environment) -> jinja2.Template:
    with importlib.resources.open_text(
        "jampdf", os.path.join("defaults", "default.html")
    ) as file:
        return env.from_string(file.read())


def parse_template(env: jinja2.Environment, data: dict[str, Any]) -> str | None:
    if data.get("layout"):
        try:
            template = env.get_template(data["layout"])
        except jinja2.TemplateNotFound:
            template = get_default_template(env)
    else:
        template = get_default_template(env)

    if not template:
        print("Das hier funktioniert vermutlich nicht wie es soll.")
        return

    return template.render(data)
