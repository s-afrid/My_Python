from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse('index.html',{'request': request})

@app.get("/page/{id}", response_class=HTMLResponse)
async def read_page(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="page.html", context={"id": id}
    )

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id":item_id, "q": q}
