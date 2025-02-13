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

browser = Browser(
	config=BrowserConfig(
		headless=False,  # This is True in production
		disable_security=True,
		new_context_config=BrowserContextConfig(
			disable_security=True,
			# minimum_wait_page_load_time=1,  # 3 on prod
			# maximum_wait_page_load_time=10,  # 20 on prod
			# no_viewport=True,
			browser_window_size={
				'width': 1280,
				'height': 1100,
			},
			# trace_path='./tmp/web_voyager_agent',
		),
	)
)

@pytest.mark.booking
@pytest.mark.asyncio
async def test_search_hotel():
    task = f"""
        Go to booking.com, type Paris to go, for the dates of {get_current_day_by_range(plus_days=2)}
        Click on Search
        Select "I'm traveling for work"
        Open the first entry and get the information about it, like location and description
    """
    agent = Agent(
		task=task,
		llm=llm,
		browser=browser,
		save_conversation_path="logs/conversation"  # Save chat logs
	)
    history = await agent.run()
    result = history.final_result()
    assert result is not None, "No result found"
    assert "Paris" in result
