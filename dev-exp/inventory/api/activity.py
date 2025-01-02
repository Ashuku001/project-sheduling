from fastapi import APIRouter, Depends
from inventory.schema.activity import ActivityCreate
from inventory.repository.activity import ActivitiesRepository
import json
from sqlalchemy.orm import Session
from config.db import sess_db

router = APIRouter()

@router.post("/activity/")
async def insert_activity(req: ActivityCreate, sess:Session = Depends(sess_db)):
    print("SESION",sess)
    activity_repo = req.model_dump()
    repo = ActivitiesRepository(sess)
    print("REPO",repo)
    results = await repo.insert_activity(activity_repo)
    return json.dumps(results)

@router.get("/activity/{id}")
async def get_activity(id: str, sess:Session = Depends(sess_db)):
    repo = ActivitiesRepository(sess)
    results = await repo.get_activity(id)
    return json.dumps(results)

@router.get("/activity/")
async def get_all_activities(sess:Session = Depends(sess_db)):
    repo = ActivitiesRepository(sess)
    results = await repo.get_all_activities()
    return json.dumps(results)

