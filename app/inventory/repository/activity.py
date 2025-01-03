from inventory.models import Activity
from typing import Dict, List, Any, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session


class ActivitiesRepository:
    """
    Repository class for managing CRUD operations on Activity table.
    """
    def __init__(self, sess:Session):
        self.sess:Session = sess

    async def insert_activity(self, activity: Activity) -> bool:
        print("activity",activity)
        try:
            self.sess.add(activity)
            await self.sess.commit()
            print(activity.id)
        except Exception as e: 
            raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
        return True