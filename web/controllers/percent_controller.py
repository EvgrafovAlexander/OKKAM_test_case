# thirdparty
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/getPercent")
async def get_percent(
        audience1: str = Query(...),
        audience2: str = Query(...)
):
    return {"aud1": audience1, "aud2": audience2}
