from aiohttp import web

async def handle(req):
    print("Got request")
    return web.FileResponse("page.html")

async def toggle(req):
    print("Toggle code goes here")
    return web.Response()

app = web.Application()
app.add_routes([web.get('/toggle', toggle), web.get('/', handle)])

web.run_app(app)