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
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, OpenAIChatPromptExecutionSettings
#, FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatHistory

# loading variables from .env file
load_dotenv()

# accessing and printing value
myKey = os.getenv("AZURE_OPENAI_API_KEY")
myEndPoint = os.getenv("AZURE_OPENAI_ENDPOINT")
myDeployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

print(myKey)
logging.basicConfig(level=logging.WARNING)

kernel = Kernel()
chat_service = AzureChatCompletion("myCC",myKey, myDeployment, myEndPoint)
kernel.add_service(chat_service)

# history = ChatHistory()
# history.add_user_message("Hi there, who are you?")
# history.add_assistant_message("I am Mosscap, a chat bot. I'm trying to figure out what people need.")

# async def chat() -> bool:
#     try:
#         user_input = input("User:> ")
#     except KeyboardInterrupt:
#         print("\n\nExiting chat...")
#         return False
#     except EOFError:
#         print("\n\nExiting chat...")
#         return False

#     if user_input == "exit":
#         print("\n\nExiting chat...")
#         return False

#     stream = True
#     if stream:
#         answer = kernel.invoke_stream(
#             chat_function,
#             user_input=user_input,
#             chat_history=history,
#         )
#         print("Mosscap:> ", end="")
#         async for message in answer:
#             print(str(message[0]), end="")
#         print("\n")
#         return True
#     answer = await kernel.invoke(
#         chat_function,
#         user_input=user_input,
#         chat_history=history,
#     )
#     print(f"Mosscap:> {answer}")
#     history.add_user_message(user_input)
#     history.add_assistant_message(str(answer))
#     return True


async def main() -> None:
    chatting = True
    # while chatting:
    #     chatting = await chat()


if __name__ == "__main__":
    asyncio.run(main())

