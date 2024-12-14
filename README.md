# tg-ghost
Small script, that let's you run a Telegram account by ChatGPT

## Config


Edit these variables in the script:

- Your user ID
`api_id = 0987654321`

- Telegram PAI hash. Replace with your own
`api_hash = '1234567890'`

- System Prompt
`system_message = "Your are an assistant. Speak German."`

- Minimal time to wait before answering
`wait_min = 60`
- Maximum time to wait before answering
`wait_max = 360`

- Users the bot will reply to, replace with valid users ids
`config_users = [00000000]`
- Bots the bot will reply to, replace with valid bot ids
`config_bots = [00000000]`
- Chats the bot will reply in. Replace with group ids
`config_chats = [00000000]`

- gpt integration - replace 0000000000 with your ChatGPT API code
`gpt_integration = GPTIntegration('000000000000')`
