# Lu

A python project made with typer to make commands to automate my work 

### Requirements
- `poetry`
- `python 3.10`

### Install

```
poetry build -> Create the .whl file
python3.10 -m pip install PATH_TO_.whl_FILE -> Install the python package
```

### Comands

- `lu crc`: Create a react component

Arguments:
- Component name: The name of the component
- Logic language: The logic language of the component [jsx/tsx]
- Style language: The style language of the component [sass/scss/css]
- Use module: Use or not the .module notation for stylesheets [True/False]
