from django.test import TestCase
from .models import *
# Create your tests here.


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class RestaurantsTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.New= Restaurants(name = 'Podzo', post ='New')
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        self.new_post= Restaurants(name = 'podzo',post = 'New',editor = self.james)
        self.new_post.save()

       


    

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.New,Restaurants))

    # Testing Save Method
    def test_save_method(self):
        self.New.save_post()
        posts = Restaurants.objects.all()
        self.assertTrue(len(posts) > 0)

    def menu_today(self):
        today_menu = Restaurants.todays_menu()
        self.assertTrue(len(today_menu)>0)

    def test_get_menu_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        menu_by_date = Restaurants.days_menu(date)
        self.assertTrue(len(menu_by_date) == 0)

    def tearDown(self):
        Editor.objects.all().delete()
        Restaurants.objects.all().delete()


