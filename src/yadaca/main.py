import click
import yadaca.commands.refresh

@click.group()
@click.version_option()
def cli():
    """Hello there, this is the CLI for yacada, a tool to help data teams document their data assets.

    This CLI lets you scaffold your data catalog and populate it with shell commands.
    """
    pass


@cli.command()
def init():
    """Initialize the configuration of your data catalog."""
    click.echo('Initialized documentation')


@cli.command()
@click.option(
    '-e', '--engine',
    required=True,
    type=click.Choice(['redshift', 'snowflake', 'bigquery', 'postgres', 'mysql'])
)
def refresh(engine: str):
    """Get metadata from one of your data systems and push it to your data catalog."""
    click.echo(f'Refreshed {engine} metadata')
    yadaca.commands.refresh.run()
