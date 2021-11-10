from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)

templates = Jinja2Templates(directory="templates")
jinja_env = templates.env

#def index(request: Request):
#    return templates.TemplateResponse('index.html',{'request': request})
@app.get("/")
def index(request:Request):
    return templates.TemplateResponse('index.html', {'request':request})