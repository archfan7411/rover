from aiohttp import web
from gpiozero import OutputDevice

relay = OutputDevice(17)
relay.off()

async def handle(req):
    print("Got request")
    return web.FileResponse("page.html")

async def toggle(req):
    relay.toggle()
    print(f"Toggled; Current value is {relay.value}")
    return web.Response()

app = web.Application()
app.add_routes([web.get('/toggle', toggle), web.get('/', handle)])

web.run_app(app)
