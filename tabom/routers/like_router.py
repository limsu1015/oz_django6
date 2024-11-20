from typing import Tuple

from django.http import HttpRequest
from ninja import Router, Schema

from tabom.models import Like
from tabom.services.like_service import do_like

router = Router()


class LikeRequest(Schema):
    user_id: int
    article_id: int


class LikeResponse(Schema):
    id: int
    user_id: int
    article_id: int


#
# @router.post("/", response={201: LikeResponse})
# def post_like(response: HttpRequest, like_request: LikeResponse) -> tuple[int, Like]:
#     like = do_like(like_request.user_id, like_request.article_id)
#     return 201, like


@router.post("/", response={201: LikeResponse})
def post_like(request: HttpRequest, like_request: LikeRequest) -> Tuple[int, Like]:
    like = do_like(like_request.user_id, like_request.article_id)
    return 201, like
