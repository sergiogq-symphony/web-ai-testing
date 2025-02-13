import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from browser_use.agent.service import Agent
from browser_use import Browser, Controller
from dotenv import load_dotenv
from utils.utils import gen_assert, get_llm
from pages.posts_page import Posts

load_dotenv()

# Initialize the model
model = get_llm()

@pytest.mark.search
@pytest.mark.asyncio
async def test_search():
    browser = Browser()
    controller = Controller(output_model=Posts)
    task = """
        Go to https://news.ycombinator.com, in the show tab get the first 5 posts
    """
    agent = Agent(task=task,
                  llm=model,
                  browser=browser,
                  controller=controller)
    history = await agent.run()

    result = history.final_result()
    assert result is not None, f"No result found, the result was {result}"
    parsed_posts: Posts = Posts.model_validate_json(result)
    assert 5 == len(parsed_posts.posts)

    task = "Navigate to 'https://en.wikipedia.org/wiki/Internet' and scroll to the 'Terminology' section and get the first paragraph there"
    agent = Agent(task=task,
                  browser=browser,
                  llm=model)
    history = await agent.run()

    result = history.final_result()
    assert result is not None, f"No result found, the result was {result}"
    assert await gen_assert("Today, the term Internet most commonly refers to the global system of interconnected computer networks, though it may also refer to any group of smaller networks", result), f"It is not included in {result}"
