'''
this explains the module to access environment variables
'''
# importing os module for environment variables
import os
import asyncio
import logging

# importing necessary functions from dotenv library
from dotenv import load_dotenv
from semantic_kernel import Kernel
#from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatHistory
from semantic_kernel.connectors.ai.open_ai import AzureChatPromptExecutionSettings
from semantic_kernel.prompt_template import InputVariable, PromptTemplateConfig

# loading variables from .env file
load_dotenv()

# accessing and printing value
myKey = os.getenv("AZURE_OPENAI_API_KEY")
myEndPoint = os.getenv("AZURE_OPENAI_ENDPOINT")
myDeployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

print(myKey)
logging.basicConfig(level=logging.WARNING)

kernel = Kernel()
chat_service = AzureChatCompletion("myCC", myKey, myDeployment, myEndPoint)
kernel.add_service(chat_service)




async def main() -> None:
    dog = 1


if __name__ == "__main__":
    asyncio.run(main())
