#!/usr/bin/env python3

# Server to control a motor connected to a PiZero.

import gpiozero

from aiohttp import web

# Corresponds to pin 11 on a PiZero
MOTOR_PIN = 17

motor = gpiozero.OutputDevice(17)

# TODO figure out whether this required 
motor.off()

# Serves the homepage
async def handle(req):
    print("Got request")
    return web.FileResponse("page.html")

# Toggles the state of the motor pin
async def toggle(req):
    motor.toggle()
    print(f"Toggled; Current value is {motor.value}")
    return web.Response()

if __name__ = "__main__":
    app = web.Application()

    # Requests to <address>/toggle should toggle, but normal
    # requests to just the address should return the home page
    app.add_routes([web.get('/toggle', toggle), web.get('/', handle)])

    web.run_app(app)
