from . import env
from openai import AsyncOpenAI, AsyncAzureOpenAI
from .threads_factory import threads_factory
from .assistants_factory import assistants_factory

# client = AsyncOpenAI(api_key=env.API_KEY, organization=env.ORG_ID)
client = AsyncAzureOpenAI(
    api_key=env.API_KEY, 
    azure_endpoint=env.AZURE_ENDPOINT,
    api_version='2024-03-01-preview',
    )
get_thread = threads_factory(client)
get_assistant, asst_filter = assistants_factory(client)
