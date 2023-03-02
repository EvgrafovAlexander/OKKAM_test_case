# thirdparty
from fastapi import APIRouter, Query

# project
from web.data import percent_data
from web.models import percent_model

router = APIRouter()


@router.get("/getPercent", response_model=percent_model.PercentModel)
async def get_percent(audience1: str = Query(...), audience2: str = Query(...)):
    return await percent_data.get_percent_data(audience1, audience2)
