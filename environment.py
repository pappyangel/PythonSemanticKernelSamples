'''
this explains the module to access environment variables
'''
# importing os module for environment variables
import os

# importing necessary functions from dotenv library
from dotenv import load_dotenv

# loading variables from .env file
load_dotenv()

# accessing and printing value
myKey = os.getenv("AZURE_OPENAI_API_KEY")

print(myKey)
