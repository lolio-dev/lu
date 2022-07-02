import typer

from lu.commands.create_react_component import create_react_component
from lu.enums.create_react_component.logic_language import LogicComponent
from lu.enums.create_react_component.style_language import StyleLanguage

app = typer.Typer()


# Register commands

@app.command()
def main():
	print('hello lolio utils')


@app.command('crc')
def cli_create_react_component(component_name: str = typer.Option('component', '-n', show_default=False, prompt=True),
                               logic_language: LogicComponent = typer.Option('ts', '-l', errors='strict', prompt=True),
                               style_language: StyleLanguage = typer.Option('scss', '-s', prompt=True),
                               use_module: bool = typer.Option(True, '-m', prompt=True)):
	"""Create react component"""

	return create_react_component(component_name, logic_language, style_language, use_module)


if __name__ == '__main__':
	app()
