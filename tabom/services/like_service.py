from django.db.models import F

from tabom.models import Article, Like


def do_like(user_id: int, article_id: int) -> Like:

    # article = Article.objects.get(id=article_id)

    like = Like.objects.create(user_id=user_id, article_id=article_id)
    Article.objects.filter(id=article_id).update(like_count=F("like_count") + 1)
    return like

    # article.like_count += 1  # 만약 like_count가 None 이 될수있다면 체크
    # article.save()


def undo_like(user_id: int, article_id: int) -> None:

    # get() 이후에 delete() 하는 방법
    # like = Like.objects.filter(user_id=user_id, article_id=article_id).delete()  # SELECT
    # like.delete()  # DELETE

    # queryset에 delete() 를 호출하는 방법
    article = Article.objects.get(id=article_id)
    delete_cnt, _ = Like.objects.filter(user_id=user_id, article_id=article_id).delete()  # DELETE
    if delete_cnt:
        article = Article.objects.get(id=article_id)
        article.like_count -= 1
        article.save()
