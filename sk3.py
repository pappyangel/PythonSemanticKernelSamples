'''
This Python program shows how to execute a chatbot using the Azure Chat Completion service.
'''
import asyncio
import logging
import os

from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
#from semantic_kernel.connectors.ai.open_ai import AzureChatPromptExecutionSettings, OpenAIChatPromptExecutionSettings
from semantic_kernel.prompt_template import PromptTemplateConfig
from semantic_kernel.prompt_template.input_variable import InputVariable
from semantic_kernel.functions import KernelArguments
from semantic_kernel.contents import ChatHistory

load_dotenv()

myKey = os.getenv("AZURE_OPENAI_API_KEY")
myEndPoint = os.getenv("AZURE_OPENAI_ENDPOINT")
myDeployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

print(myKey)
logging.basicConfig(level=logging.WARNING)

kernel = Kernel()
#chat_service = AzureChatCompletion("myCC",myKey, myDeployment, myEndPoint)
chat_service = AzureChatCompletion("myCC")
kernel.add_service(chat_service)

prompt = """
ChatBot can have a conversation with you about any topic.
It can give explicit instructions or say 'I don't know' if it does not have an answer.

{{$history}}
User: {{$user_input}}
ChatBot: """

#execution_settings = AzureChatPromptExecutionSettings()
#execution_settings = AzureChatPromptExecutionSettings(max_tokens=2000, temperature=0.7, top_p=1.0)

prompt_template_config = PromptTemplateConfig(
    template=prompt,
    name="chat",
    template_format="semantic-kernel",
    input_variables=[
        InputVariable(name="user_input", description="The user input", is_required=True),
        InputVariable(name="history", description="The conversation history", is_required=True),
    ]
    #,    execution_settings=execution_settings,
)

chat_function = kernel.add_function(
    function_name="chat",
    plugin_name="chatPlugin",
    prompt_template_config=prompt_template_config,
)

chat_history = ChatHistory()
chat_history.add_system_message("You are a helpful chatbot who is good about giving book recommendations.")
arguments = KernelArguments(user_input="Hi, I'm looking for book suggestions", history=chat_history)


async def main() -> None:
    
    response = await kernel.invoke(chat_function, arguments)
    print(response)
    chat_history.add_assistant_message(str(response))



if __name__ == "__main__":
    asyncio.run(main())



