import os
import subprocess

import click


@click.command()
@click.argument('path', default=os.path.join('sushy', 'tests'))
def cli(path):
    """
        Run test with pytest
    """
    cmd = 'py.test {0}'.format(path)
    return subprocess.call(cmd, shell=True)
