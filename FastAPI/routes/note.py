from fastapi import APIRouter, Request
from models.note import Note
from config.db import conn
from schema.note import note_to_dict, note_list

from fastapi.responses import HTMLResponse

note = APIRouter()

@note.get('/')
async def read_note():
    return {"message": "Root of route note"}

