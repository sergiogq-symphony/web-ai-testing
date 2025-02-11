import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama

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
