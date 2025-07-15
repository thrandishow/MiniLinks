from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.schemas import UrlCreate
from app.services import generate_short_id
from app.models import Url

Base.metadata.create_all(bind=engine)
app = FastAPI(title="MiniLinks")


@app.get("/")
async def say_hello():
    return "Hello world"


@app.post("/shorten/")
async def shorten_url(item: UrlCreate, db: Session = Depends(get_db)):
    short_id = generate_short_id()
    while True:
        result = db.query(Url).filter(Url.id == short_id).first()
        if not result:
            break
        short_id = generate_short_id()
    db_url = Url(id=short_id, original_url=item.url)
    db.add(db_url)
    db.commit()
    return {"short_url": f"https://{short_id}"}


@app.get("/{short_id}")
async def redirect_to_url(short_id: str, db: Session = Depends(get_db)):
    url_entry = db.query(Url).filter(Url.id == short_id).first()
    if not url_entry:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=url_entry.original_url)
