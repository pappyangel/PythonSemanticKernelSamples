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

prompt = """{{$input}}
Summarize the content above.
"""


execution_settings = AzureChatPromptExecutionSettings(
        # service_id= service_id,
        # ai_model_id="gpt-35-turbo",
        max_tokens=2000,
        temperature=0.7,
    )

prompt_template_config = PromptTemplateConfig(
    template=prompt,
    name="summarize",
    template_format="semantic-kernel",
    input_variables=[
        InputVariable(name="input", description="The user input", is_required=True),
    ]
     , execution_settings=execution_settings
)

summarize = kernel.add_function(
    function_name="summarizeFunc",
    plugin_name="summarizePlugin",
    prompt_template_config=prompt_template_config,
)

input_text = """
Tom Brady won a super bowl in the first year he played in the NFL.
Tom Brady won the super bowl 9 times in his 20 year career.
He retired after winning a super bowl with the Tampa Bay Bucs.
"""



async def main() -> None:
    
    summary = await kernel.invoke(summarize, input = input_text)

    print(summary)



if __name__ == "__main__":
    asyncio.run(main())
