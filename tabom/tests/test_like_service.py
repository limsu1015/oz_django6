from django.test import TestCase

from tabom.models import Article, User
from tabom.sevices.like_service import do_like


class Test_like_service(TestCase):
    def g_a_user_can_like_on_article(self) -> None:
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # when
        like = do_like(user.id, article.id)

        # then
        # id 가 들어있다는 것은 데이터베이스로부터 id를 발급받았다는 뜻
        # 즉, 성공적으로 insert 가 되었다는 증거입니다.
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user.id)
        self.assertEqual(article.id, like.article.id)
