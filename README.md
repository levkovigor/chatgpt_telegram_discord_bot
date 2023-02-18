# chatgpt_telegram_discord_bot

> ### This is a project that provides you to build your own Discord bot using ChatGPT
>
> ⭐️ If this repo helps you, a star is the biggest support for me and also helps you stay up-to-date 

## Features

* `/chat [message]` Chat with ChatGPT!
* `/gpt3 [message]' Chat with GPT-3 when ChatGPT is not working
* `/reset`   ChatGPT conversation history will be erased

### Chat

![image](https://user-images.githubusercontent.com/89479282/206497774-47d960cd-1aeb-4fba-9af5-1f9d6ff41f00.gif)

# Setup

## Install

1. `pip install -r requirements.txt`

## Step 1: Create a Telegram bot

Open Telegram messenger, sign in to your account or create a new one.

1. Enter @Botfather in the search tab and choose this bot.

Official Telegram bots have a blue checkmark beside their name.

![image](https://www.spcdn.org/images/En-knowledge_base/chatbots/telegram/create-bot/scr1-min.png)

Click “Start” to activate BotFather bot.

![image](https://www.spcdn.org/images/En-knowledge_base/chatbots/telegram/create-bot/scr2-min.png)

In response, you receive a list of commands to manage bots.

2. Choose or type the /newbot command and send it.

![image](https://www.spcdn.org/images/En-knowledge_base/chatbots/telegram/create-bot/scr3-min.png)

3. Choose a name for your bot — your subscribers will see it in the conversation. And choose a username for your bot — the bot can be found by its username in searches. The username must be unique and end with the word “bot.”

![image](https://www.spcdn.org/images/En-knowledge_base/chatbots/telegram/create-bot/scr4-min.png)

After you choose a suitable name for your bot — the bot is created. You will receive a message with a link to your bot t.me/<bot_username>, recommendations to set up a profile picture, description, and a list of commands to manage your new bot.

4. Store the token to `config.dev.json` under the `telegram_chat_gpt_API_key`

![image](https://www.spcdn.org/images/En-knowledge_base/chatbots/telegram/create-bot/scr5-min.png)

## Step 1: Create a Discord bot

1. Go to https://discord.com/developers/applications create an application
2. Build a Discord bot under the application
3. Get the token from bot setting

   ![image](https://user-images.githubusercontent.com/89479282/205949161-4b508c6d-19a7-49b6-b8ed-7525ddbef430.png)
4. Store the token to `config.dev.json` under the `discord_bot_token`

   ![image](https://user-images.githubusercontent.com/89479282/207357762-94234aa7-aa55-4504-8dfd-9c68ae23a826.png)
   
5. Turn MESSAGE CONTENT INTENT `ON`

   ![image](https://user-images.githubusercontent.com/89479282/205949323-4354bd7d-9bb9-4f4b-a87e-deb9933a89b5.png)
   
6. Invite your bot to your server via OAuth2 URL Generator

   ![image](https://user-images.githubusercontent.com/89479282/205949600-0c7ddb40-7e82-47a0-b59a-b089f929d177.png)

## Step 2: Geanerate a OpenAI API key

1. Go to https://beta.openai.com/account/api-keys

2. Click Create new secret key

   ![image](https://user-images.githubusercontent.com/89479282/207970699-2e0cb671-8636-4e27-b1f3-b75d6db9b57e.PNG)

2. Store the SECRET KEY to `config.dev.json` under the `openAI_key`

## Step 3: Run the bot on the desktop
1. Open a terminal or command prompt
2. Navigate to the directory where you installed the ChatGPT Discord bot
3. Run `python3 main.py` to start the bot

## Step 3: Run the bot with docker

1. Build the Dcoker image & Run the Docker container `docker compose up -d`
2. Inspect whether the bot works well `docker logs -t chatgpt-discord-bot`

   ### Stop the bot:

   * `docker ps` to see the list of running services
   * `docker stop <BOT CONTAINER ID>` to stop the running bot

### Have A Good Chat !

## Optional: Setup starting prompt

* A starting prompt would be invoked when the bot is first started or reset
* You can set it up by modifying the content in `starting-prompt.txt`
* All the text in the file will be fired as a prompt to the bot  
* Get the first message from ChatGPT in your discord channel!

   1. Right-click the channel you want to recieve the message, `Copy  ID`
   
        ![channel-id](https://user-images.githubusercontent.com/89479282/207697217-e03357b3-3b3d-44d0-b880-163217ed4a49.PNG)
    
   2. paste it into `config.dev.json` under `discord_channel_id `
