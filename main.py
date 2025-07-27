from meshagent.agents.chat import ChatBot
from meshagent.api.services import ServiceHost
from meshagent.openai import OpenAIResponsesAdapter
import asyncio
import os

system_prompt = os.getenv("SYSTEM_PROMPT")

print(f"starting service with rule: {system_prompt}")

host = ServiceHost()

@host.path("/agent")
class MyChatBot(ChatBot):
  def __init__(self):
    super().__init__(
      name="chatbot",
      rules=[ system_prompt ],
      llm_adapter=OpenAIResponsesAdapter(),
    )

asyncio.run(host.run())

