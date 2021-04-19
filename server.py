from aiohttp import web
from gpiozero import OutputDevice


PIN = 17
relay = OutputDevice(PIN)
relay.off()


# Returns homepage
async def handle(req):
    print("Got request")
    return web.FileResponse("page.html")


# Toggles the LED
async def toggle(req):
    relay.toggle()
    print(f"Toggled; Current value is {relay.value}")
    return web.Response()


# Configure aiohttp
app = web.Application()
app.add_routes([
    web.get('/toggle', toggle), 
    web.get('/', handle),
])

web.run_app(app)
