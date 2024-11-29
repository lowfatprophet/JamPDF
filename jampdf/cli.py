import os

import click
import tomllib

from jampdf.config import create_config, read_config
from jampdf.markdown import parse_input
from jampdf.template import parse_template, template_env


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, default=False, help="Show version.")
def cli(version=False) -> None:
    if version:
        with open("pyproject.toml", "rb") as file:
            config = tomllib.load(file)
            click.echo(f"Version: {config['tool']['poetry']['version']}")


@cli.command(help="Creates a new project directory in current directory.")
@click.argument("dir_name", required=True)
@click.option("--config", "-c", required=False)
def new(dir_name="", config: str | None = None) -> None:
    click.echo(f"Initialize a new project in {dir_name}.")

    path = os.path.join(dir_name)

    if not os.path.exists(path):
        os.makedirs(path)

    os.chdir(dir_name)
    create_directories()

    if config:
        click.echo(f"{config} was provided as config file.")
        _config = read_config(config)
    else:
        _config = create_config()


@cli.command(help="Initialize a new project in current directory.")
@click.option("--config", "-c", required=False)
def init(config: str) -> None:
    click.echo("Initialize project in current folder.")

    if os.listdir("."):
        click.confirm("Directory not empty. Continue?", abort=True)

    if config:
        click.echo(f"{config} was provided as config file.")
        _config = read_config(config)
    else:
        _config = create_config()


@cli.command(help="Build project.")
@click.option("--outdir", "-o", default="_dist", required=False)
def build(outdir="_dist") -> None:
    input_files = os.walk(os.path.join("_content"))
    env = template_env()

    for dirpath, dirnames, filenames in input_files:
        for file in filenames:
            file_basename = ".".join(file.split(".")[:-1])
            with open(os.path.join(dirpath, file), "r") as input_file:
                text = input_file.read()
                # data = parse_frontmatter(text)
                data, content = parse_input(text)
                data["content"] = content

                html = parse_template(env, data)

            if not html:
                continue

            with open(
                os.path.join(outdir, f"{file_basename}.html"), "w+", encoding="utf-8"
            ) as output_file:
                output_file.write(html)


def create_directories() -> None:
    for dir in ["_content", "_dist", "_templates"]:
        os.makedirs(os.path.join(dir))


if __name__ == "__main__":
    cli()
