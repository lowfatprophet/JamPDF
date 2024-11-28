import os

import click

from jampdf.config import create_config, read_config


@click.group()
def cli() -> None:
    pass


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
@click.option("--outdir", "-o", required=False)
def build(outdir="_dist") -> None:
    pass


def create_directories() -> None:
    for dir in ["_content", "_templates"]:
        os.makedirs(os.path.join(dir))


if __name__ == "__main__":
    cli()
