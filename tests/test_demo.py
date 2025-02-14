import pytest
import os

from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-exp',
            api_key=os.getenv("GEMINI_API_KEY"))

@pytest.mark.demo
@pytest.mark.asyncio
async def test_demo():
    prompt = """
        Go to Airbnb, search for an apartment in Paris and get the price of the first one
    """
    agent = Agent(
        task=prompt,
        llm=llm,
    )
    result = await agent.run()
    assert result is not None, f"No result found, the result was {result}"
