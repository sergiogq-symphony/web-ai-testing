import os
import asyncio

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama
from datetime import datetime, timedelta
from google import genai


def get_llm():
    if os.getenv("GEMINI_API_KEY"):
        return ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-exp',
            api_key=os.getenv("GEMINI_API_KEY"))
    elif os.getenv("OPENAI_API_KEY"):
        return ChatOpenAI(model="gpt-4o")
    elif os.getenv("ANTHROPIC_API_KEY"):
        return ChatAnthropic(
            model_name="claude-3-5-sonnet-20240620",
            temperature=0.0,
            timeout=100) # Increase for complex tasks
    elif os.getenv("DEEPSEEK_API_KEY"):
        return ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-reasoner',
            api_key=os.getenv("DEEPSEEK_API_KEY"))
    else:
        return ChatOllama(model="qwen2.5", num_ctx=32000)


def get_current_day_by_range(plus_days=182, range=7):
    # Get the current date
    current_date = datetime.today()

    # Add 6 months (approximate as 182 days)
    future_start_date = current_date + timedelta(days=plus_days)
    future_end_date = future_start_date + timedelta(days=range)  # Assuming a 7-day stay

    # Format the dates as "Month Day-Day, Year"
    return f"{future_start_date.strftime('%B %d')}-{future_end_date.strftime('%d, %Y')}"


async def gen_assert(text, content):
    prompt = f"""
    Compare the following two texts:

    Text 1: {text}
    Text 2: {content}

    Return only "True" if they are similar or contain the same meaning, or are very similar in content (it is included).
    Otherwise, return only "False". Do not provide explanations, just the boolean value.
    """

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = await asyncio.to_thread(
        client.models.generate_content,
        model="gemini-2.0-flash",
        contents=prompt
    )

    result = response.text.strip()  # Ensure clean output
    return result.lower() == "true"  # Convert to a boolean
