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

    async def insert_activity(self, details: Dict[str, Any]) -> bool:
        print("DETAILS",details)
        try:
            activity = Activity(**details)
            print("ACITIVTY",activity)
            results = await self.sess.add(activity)
            print("RESULTS",results)
            return results
        except Exception as e:
            print(e)
            raise HTTPException(500, detail=f"Error inserting activity: {e}")

    async def update_activity(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            activity = await Activity.objects().get(Activity.id == id)
            for key, value in details.items():
                setattr(activity, key, value)
            await activity.save()
            return True
        except Exception as e:
            raise HTTPException(500, f"Error updating activity: {e}")

    async def delete_activity(self, id: int) -> bool:
        try:
            activity = await Activity.objects().get(Activity.id == id)
            await activity.remove()
            return True
        except Exception as e:
            raise HTTPException(500, f"Error deleting activity: {e}")

    async def get_all_activities(self) -> List[Activity]:
        try:
            return await Activity.select().order_by(Activity.id)
        except Exception as e:
            raise HTTPException(500, f"Error retrieving activities: {e}")

    async def get_activity(self, id: int) -> Optional[Activity]:
        try:
            return await Activity.objects().get(Activity.id == id)
        except Exception as e:
            raise HTTPException(500, f"Error retrieving activity: {e}")