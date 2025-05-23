import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig
from dotenv import load_dotenv
from utils.utils import get_current_day_by_range, get_llm

load_dotenv()

# Initialize the model
llm = get_llm()

@pytest.mark.symphony
@pytest.mark.asyncio
async def test_symphony_chat():
    prompt = """
        Go to symphony.com and get the title of the top of the page
    """
    agent = Agent(
        task=prompt,
        llm=llm,
    )
    result = await agent.run()
    assert result is not None, f"No result found, the result was {result}"
