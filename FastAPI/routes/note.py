from fastapi import APIRouter, Request
from models.note import Note
from config.db import conn
from schema.note import note_to_dict, note_list

from fastapi.responses import HTMLResponse

note = APIRouter()

@note.get('/')
async def read_note():
    return {"message": "Root of route note"}

@note.post('/')
async def read_data(note_data: Note):
    data = dict(note_data)
    result = conn.Note.notes.insert_one(data)
    return {"received": {"message":"Save to DB","id": str(result.inserted_id)}}