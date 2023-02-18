#from revChatGPT.Official import Chatbot
from revChatGPT.Official import AsyncChatbot
import openai
from asgiref.sync import sync_to_async
from telebot.async_telebot import AsyncTeleBot
from src import getconfig

config = getconfig.get_config()
openai.api_key = config['openAI_key']
#chatbot = Chatbot(api_key=config['openAI_key'])
chatbot = AsyncChatbot(api_key=config['openAI_key'], engine="text-davinci-003")
telegramChatGPTBot = ""
if (config['bot'] == "telegram"):
    telegramChatGPTBot = AsyncTeleBot(config['telegram_chat_gpt_API_key'])

async def handle_response_chat(message) -> str:
    #response = await sync_to_async(chatbot.ask)(message)
    response = await chatbot.ask(message)
    responseMessage = response["choices"][0]["text"]

    return responseMessage
    
async def handle_response_gpt(message) -> str:
    response = await sync_to_async(openai.Completion.create)(
        model="text-davinci-003",
        prompt=message,
        temperature=1.0,
        max_tokens=512,
        top_p=0.9
    )

    responseMessage = response.choices[0].text

    return responseMessage