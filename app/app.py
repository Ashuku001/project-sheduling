from fastapi import FastAPI

from inventory.api.activity import router as activity_router

app =  FastAPI()

app.include_router(activity_router, prefix="/activity", tags=["activity"])