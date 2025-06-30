import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig
from dotenv import load_dotenv
from utils.utils import get_llm

load_dotenv()

# Initialize the model
llm = get_llm()

@pytest.mark.symphony
@pytest.mark.asyncio
async def test_symphony_home_page():
    prompt = """
        Go to symphony.com and get the title of the top of the page
    """
    agent = Agent(
        task=prompt,
        llm=llm,
    )
    history = await agent.run()
    result = history.final_result()
    print(f"Result: {result}")
    assert result is not None, f"No result found, the result was {result}"
    assert "Symphony Communication | Messaging Software for Finance" in result
