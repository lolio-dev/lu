from pathlib import Path

from typer import echo, style, colors

from lu.enums.create_react_component.logic_language import LogicComponent
from lu.enums.create_react_component.style_language import StyleLanguage


def create_react_component(component_name: str,
                           logic_language: LogicComponent,
                           style_language: StyleLanguage,
                           use_module: bool):
	component_path = Path(f'{Path().absolute()}/{component_name}')

	try:
		component_path.mkdir(parents=True, exist_ok=False)
	except FileExistsError:
		echo(style('Component already exists', fg=colors.RED))

	component_logic_path = Path(f'{component_path}/{component_name}.{logic_language}x')
	component_style_path = Path(f'{component_path}/{component_name}{".module" if use_module else ""}.{style_language}')

	component_logic_path.touch(), component_style_path.touch()

	capitalized_component_name = ''.join([i.capitalize() for i in component_name.split('-')])

	template = Path(f'{Path(__file__).parent.absolute().parent.absolute()}/templates/react_component.{logic_language}x').read_text().replace('$component$', capitalized_component_name)

	component_logic_path.write_text(template)
