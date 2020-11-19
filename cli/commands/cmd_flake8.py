import subprocess

import click


@click.command()
@click.option(
    '--skip-init/--no-skip-init',
    default=True,
    help='Skip __init__.py files? '
)
@click.argument('path', default='sushy')
def cli(skip_init, path):
    """
        Run flake8  to analyze the code base.
    """

    flake8_flag_exclude = ''
    if skip_init:
        flake8_flag_exclude = ' --exclude __init__.py'

    cmd = 'flake8 {0}{1}'.format(path, flake8_flag_exclude)
    return subprocess.call(cmd, shell=True)
