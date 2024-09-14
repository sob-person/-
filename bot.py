import webserver
import discord
INTENTS = discord.Intents.all()
client = discord.Client(intents = INTENTS)
# Discord 클라이언트 객체 생성

# 봇이 준비되었을 때 실행되는 이벤트 핸들러
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# 봇이 메시지를 받았을 때 실행되는 이벤트 핸들러
@client.event
async def on_message(message):
    # 메시지를 보낸 사람이 봇 자신이면 무시
    if message.author == client.user:
        return

    if message.content.startswith('!안녕'):
        await message.channel.send('안녕하세요!')

# 디스코드 봇 토큰을 사용하여 봇 로그인
# 여기에는 본인이 발급받은 디스코드 봇 토큰을 입력해야 합니다.
client.run('MTI4NDQ2MTY2NDQwNTU1MzE5Nw.GJF2IE.m5rNM-cWgCg-p2wxb0OEUNZMEsxfgX9WKDgEhU')
