from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    return Like.objects.create(user_id=user_id, article_id=article_id)


def undo_like(user_id: int, article_id: int) -> None:

    # get() 이후에 delete() 하는 방법
    # like = Like.objects.filter(user_id=user_id, article_id=article_id).delete()  # SELECT
    # like.delete()  # DELETE

    # queryset에 delete() 를 호출하는 방법
    Like.objects.filter(user_id=user_id, article_id=article_id).delete()  # DELETE
