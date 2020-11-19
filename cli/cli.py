import os

import click

cmd_folder = os.path.join(os.path.dirname(__file__), 'commands')
cmd_prefix = 'cmd_'


class CLI(click.MultiCommand):

    def list_commands(self, ctx):
        """
            Obtain a list of all variable commands.
        """

        commands = []
        for file_name in os.listdir(cmd_folder):
            if file_name.endswith('py') and file_name.startswith(cmd_prefix):
                commands.append(file_name[4:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        """
            Get command by name.
        """
        ns = {}
        file_name = os.path.join(cmd_folder, cmd_prefix + name + '.py')
        print(file_name)
        with open(file_name) as f:
            code = compile(f.read(), file_name, 'exec')
            eval(code, ns, ns)
        return ns['cli']


@click.command(cls=CLI)
def cli():
    """
        Commands to help manage project.
    """
    pass
