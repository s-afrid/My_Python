from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union

# import mongoclient
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Establish connection to mongoDB
conn = MongoClient('mongodb+srv://s-afrid:Af02052002@cluster0.ht9jcbk.mongodb.net/?appName=Cluster0')

try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.get('/',response_class=HTMLResponse)
async def read_home(request: Request):
    docs = conn.Note.notes.find({})
    newDocs = []
    for d in docs:
        newDocs.append(
            {
                "id": d["_id"],
                "note": d["note"]
            }
        )
    print(newDocs)
    return templates.TemplateResponse('index.html',{'request': request, "newDocs" : newDocs})

@app.get("/page/{id}", response_class=HTMLResponse)
async def read_page(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="page.html", context={"id": id}
    )

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id":item_id, "q": q}
