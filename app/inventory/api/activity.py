from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
import json
from sqlalchemy.orm import Session

from inventory.schema.activity import ActivityCreate
from inventory.repository.activity import ActivitiesRepository
from inventory.models import Activity
from config.db import get_async_session

router = APIRouter()

@router.post("/activity/")
async def insert_activity(req: ActivityCreate, sess:Session = Depends(get_async_session)):
    repo = ActivitiesRepository(sess)
    activity = Activity(**req.model_dump())
    result = await repo.insert_activity(activity)
    if result == True:
        return activity
    else: 
        return JSONResponse(content={'message':'create activity problem encountered'}, status_code=500)

@router.get("/activity/{id}/")
async def get_activity(id: str, sess:Session = Depends(get_async_session)):
    repo = ActivitiesRepository(sess)
    results = await repo.get_activity(id)
    return json.dumps(results)

@router.get("/activity/")
async def get_all_activities(sess:Session = Depends(get_async_session)):
    repo = ActivitiesRepository(sess)
    results = await repo.get_all_activities()
    return json.dumps(results)

