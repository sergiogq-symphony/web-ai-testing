# Web AI testing
Let's use AI (LMMs) to tests Web sites (UI).

![Demo](/auto-demo.gif)

## Example
With a simple text prompt, like shown below, the framework is able to understand the goal and going to the browser to achieve it without human intervention.

```py
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-exp',
            api_key=os.getenv("GEMINI_API_KEY"))

@pytest.mark.asyncio
async def test_booking():
    prompt = """
        Go to Airbnb, search for an apartment in Paris and get the price of the first one
    """
    agent = Agent(
        task=prompt,
        llm=llm,
    )
    result = await agent.run()
    assert result is not None, f"No result found, the result was {result}"
```

## Setup (Linux)
```sh
# Use UV (https://docs.astral.sh/uv)
curl -LsSf https://astral.sh/uv/install.sh | sh

uv venv --python 3.11
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# NOTE: Clone the `.env.example` file to `.env` name and add the `GEMINI_API_KEY` 
# value obtained from https://aistudio.google.com/u/1/apikey site 
# (it will generate charges on the GCP account billing)
```

## Execution
```sh
pytest -s

# Run with tags
pytest -s -m "not shopping and booking"
```

## References
- https://playwright.dev/python/docs/library
- https://github.com/browser-use/browser-use?tab=readme-ov-file
- https://docs.browser-use.com/customize/supported-models
