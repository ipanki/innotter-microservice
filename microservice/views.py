from fastapi import APIRouter, Depends

from microservice.service import get_page_statistics
from microservice.authentication import auth
routes_user = APIRouter()


@routes_user.get("/pages/{page_id}/statistics/", dependencies=[Depends(auth)])
def get_statistics(page_id: str):
    return get_page_statistics(page_id)
