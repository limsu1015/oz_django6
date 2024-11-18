from tabom.models import Article


def get_an_article(article_id: int) -> Article:
    article = Article.objects.get(id=article_id)
    return article
