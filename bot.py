from plugins import web_server
from aiohttp import web

TIMEZONE = "Asia/Kolkata"

class Bot(Client):
    async def start(self):
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", "8080").start()
        
app = Bot()
app.run()
