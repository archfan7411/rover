# aiohttp will be used to create the webserver
from aiohttp import web
# gpiozero's OutputDevice class is suffificient for our needs
from gpiozero import OutputDevice

# Creates the OutputDevice relay, controlling GPIO pin 17
relay = OutputDevice(17)

# Sets the pin as off. Not sure if this is required.
relay.off()

# Handles requests for the home page
async def handle(req):
    print("Got request")
    # Returns the HTML file for viewing
    return web.FileResponse("page.html")

# Handles requests to toggle the pin
async def toggle(req):
    # Toggles the relay
    relay.toggle()
    print(f"Toggled; Current value is {relay.value}")
    return web.Response()

app = web.Application()

# Requests to <address>/toggle should toggle, but normal
# requests to just the address should return the home page
app.add_routes([web.get('/toggle', toggle), web.get('/', handle)])

# Starts the server, a blocking call
web.run_app(app)
