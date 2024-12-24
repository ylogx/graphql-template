import click

from loguru import logger

import graphql_trial.performer


@click.group()
def cli():
    pass


@cli.command()
def perform():
    performance = graphql_trial.performer.perform_something()
    logger.info(f"Performance output: {performance}")


if __name__ == "__main__":
    cli()
