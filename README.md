

## Setup

1. Install [`poetry`](https://python-poetry.org/docs/#installing-with-pipx)
2. Create `venv`
3. Run `poetry install`
4. Install [`tesseract`](https://github.com/tesseract-ocr/tesseract#installing-tesseract)
     - Note that you must be able to invoke the tesseract command as tesseract. If this isn't the case,
    for example because tesseract isn't in your PATH, you will have to set path to your tesseract executable in `.env` file in the project directory.

## Development

Formatting, lint, typecheck:

```shell
poe fmt
```
