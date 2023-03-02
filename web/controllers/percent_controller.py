# thirdparty
from fastapi import APIRouter, Query

# project
from web.data import percent_data

router = APIRouter()


@router.get("/getPercent")
async def get_percent(audience1: str = Query(...), audience2: str = Query(...)):
    result = await percent_data.get_percent_data(audience1, audience2)
    return result
