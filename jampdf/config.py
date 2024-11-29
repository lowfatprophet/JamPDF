import json
import os

import click
import tomllib
import yaml

from jampdf.custom_types import Config


def create_config(root="") -> Config:
    config: Config = {
        "title": None,
        "description": None,
        "name": None,
        "email": None,
        "combine_output": False,
        "page_size": "DIN A4",
    }
    config["title"] = click.prompt(
        "Title", default=os.path.dirname(os.path.realpath(__file__)), show_default=False
    )
    config["description"] = click.prompt("Description", default="", show_default=False)
    config["name"] = click.prompt("Name", default="", show_default=False)
    config["email"] = click.prompt("Email", default="", show_default=False)

    with open(
        os.path.join(".", root, "_config.yaml"), "w", encoding="utf-8"
    ) as config_file:
        config_file.write(yaml.dump(config, Dumper=yaml.Dumper))

    return config


def read_config(config_file: str) -> Config | None:
    try:
        file_ext = config_file.split(".")[-1]
        with open(config_file, "rb") as file:
            if file_ext == "yaml":
                return yaml.load(file, Loader=yaml.Loader)
            elif file_ext == "toml":
                return tomllib.load(file)  # type: ignore
            elif file_ext == "json":
                return json.load(file)
    except FileNotFoundError:
        click.echo("Config file cannot be read.")
