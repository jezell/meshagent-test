from meshagent.agents.chat import ChatBot
from meshagent.api.services import ServiceHost
from meshagent.openai import OpenAIResponsesAdapter
import asyncio

print("starting service")

host = ServiceHost()

@host.path("/agent")
class MyChatBot(ChatBot):
  def __init__(self):
    super().__init__(
      name="chatbot",
      llm_adapter=OpenAIResponsesAdapter(),
    )

asyncio.run(host.run())

