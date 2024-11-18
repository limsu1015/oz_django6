from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, Like, User
from tabom.services.like_service import do_like, undo_like


class TestlikeService(TestCase):

    def test_a_user_can_like_on_article(self) -> None:
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

    def test_a_user_can_like_on_article_only_once(self) -> None:
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        like1 = do_like(user.id, article.id)
        # exception 이 발생 하면 통과, 아무 일도 안 일어나면 assertionError 를 일으킨다
        with self.assertRaises(IntegrityError):
            do_like(user.id, article.id)

    def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
        # Given
        invalid_user_id = 9988
        article = Article.objects.create(title="test_title")

        # Expect
        with self.assertRaises(IntegrityError):
            do_like(invalid_user_id, article.id)

    def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
        # Given
        user = User.objects.create(name="test")
        invalid_article_id = 9988

        # Expect
        with self.assertRaises(IntegrityError):
            do_like(user.id, invalid_article_id)

    def test_like_count_should_increase(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        do_like(user.id, article.id)

        # Then
        result_articles = Article.objects.get(id=article.id)
        self.assertEqual(1, article.like_set.count())

    def test_a_user_can_undo_like(self) -> None:
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")
        like = Like.objects.create(user_id=user.id, article_id=article.id)

        # When
        undo_like(user.id, article.id)

        # Then
        with self.assertRaises(like.DoesNotExist):
            Like.objects.get(id=like.id)

        # Then 절에서 DoesNotExist 로 검사하는거 말고 방법이 있지 않을까?
