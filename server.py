from aiohttp import web
import urllib.request

import json
import ssl
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context


routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

@routes.get('/api/v1/{m}')
async def hello(request):
    t=datetime.now().strftime("%H:%M:%S")
    newpath="https://finnhub.io/%s" % request.path_qs
    #print(newpath)
    with urllib.request.urlopen(newpath,timeout=3) as f:
        output=f.read().decode('utf-8')
    jj=json.loads(output)
    jj['time']=t
    output=json.dumps(jj)
    return web.Response(text = output)


app = web.Application()
app.add_routes(routes)
web.run_app(app,port=18080)

