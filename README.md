# JamPDF

## Installation

Make sure to have Python >= 3.11 & [pipx](https://pipx.pypa.io/latest/installation/) installed.

```shell
pipx install jampdf
```

JamPDF gets installed in pipx's global application directory and is accessible system-wide.

## Usage

### Creating a new project

There are two ways to initialize a new project:

1. [`new`](#new): Pass along a valid directory name and JamPDF creates a project inside a newly created directory.
2. [`init`](#init): 

### File structure

JamPDF relies on a strict file pattern (for now):

```
root
├─ _templates
|  ├─ *.html
├─ _content
|  ├─ posts
|  |  ├─ *.md
|  ├─ pages
|  |  ├─ *.md
|  ├─ *.md
├─ _config.{json, yaml, toml}
├─ assets
├─ _dist
```

The `_content` directory is where you would then place your content in arbitrary structure. Place HTML-layouts in the `_templates` folder.

### Configuration

Configuration is done in `_config.yaml`, placed in the project's root folder.

### Commands

#### `new`

Create new directory with given name and initialize a new project.

#### `init`

Initialize a new project inside the current folder.

#### `build`

Build the project.

## Development

Dependency installation and package distribution is handled through [Poetry](https://python-poetry.org).