# Web AI testing
Let's use AI (LMMs) to tests Web sites (UI)

## Setup (Linux)
```sh
# Use UV (https://docs.astral.sh/uv)
curl -LsSf https://astral.sh/uv/install.sh | sh

uv venv --python 3.11
source .venv/bin/activate

# Install dependencies
uv pip install browser-use playwright pytest-playwright pytest-asyncio pytest pytest-html

# NOTE: Clone the `.env.example` file to `.env` name and add the `GEMINI_API_KEY` value obtained from https://aistudio.google.com/u/1/apikey site
```

## Run
```sh
pytest --html=report.html --self-contained-html
```

## References
- https://playwright.dev/python/docs/library
- https://github.com/browser-use/browser-use?tab=readme-ov-file
- https://docs.browser-use.com/customize/supported-models
