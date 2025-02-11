import pytest
import os
import asyncio
import pytest_asyncio
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from browser_use.browser.context import BrowserContextConfig, BrowserContext
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from utils.utils import get_llm

load_dotenv()

# Initialize the model
llm = get_llm()

@pytest_asyncio.fixture(scope="function")
async def browser():
    async with async_playwright() as p:
        # Reuse existing browser
        browser = Browser()
        yield browser # Provide browser instance to tests
        await browser.close() # Cleanup after tests


@pytest.mark.asyncio
async def test_search_and_add_cart(browser):
    # Use specific browser context (preferred method)
    async with await browser.new_context() as context:
        task1 = """
            Go to Amazon.com, search for 'Lenovo IdeaPad laptop', open the first item and get the information about it, like name, brand, model, screen size.
        """
        agent = Agent(
            task=task1,
            llm=llm,
            browser_context=context # Use persistent context
        )
        history = await agent.run()
        result = history.final_result()
        assert result is not None, f"No item found in  {result}"
        assert "Lenovo" in result

        task2 = """
            Add the item to the cart and get how many items there are into the shooping cart
        """
        agent = Agent(
            task=task2,
            llm=llm,
            browser_context=context # Use persistent context
        )
        history = await agent.run()
        result = history.final_result()
        assert result is not None, "No result found"
        assert "1" in result, f"Expected 1 item in cart, but got {result}"
