from django.test import TestCase
from .models import Editor,Article,tags,Category,Location
import datetime as dt

class EditorTestClass(TestCase):

    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Odera', email ='james@odera.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Odera', email ='james@odera.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_Category = Category(name = 'testing')
        self.new_Category.save()

        self.new_Location = Location(name = 'testing')
        self.new_Location.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_get_album_today(self):
        today_album = Article.todays_album()
        self.assertTrue(len(today_album)>0)

    def test_get_album_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        album_by_date = Article.days_album(date)
        self.assertTrue(len(album_by_date) == 0)

    @classmethod
    def days_album(cls,date):
        album = cls.objects.filter(pub_date__date = date)
        return album