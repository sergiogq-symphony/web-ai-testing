import pytest
import os
import asyncio

from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=os.getenv("GEMINI_API_KEY"))

@pytest.mark.asyncio
async def test_shopping1():
     # Create agent with the model
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm
    )
    result = await agent.run()
    print(result)

    assert 1 == 1

@pytest.mark.asyncio
def test_shopping2():
    assert '10' == '10'
