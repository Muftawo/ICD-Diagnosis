from django.test import TestCase
from api.models import Code,Category
from django.contrib.auth.models import User
from model_bakery import baker

class CodeTest(TestCase):
    """This class defines the test suite for the Code model."""
    
    def setUp(self):
        """Define the test client and other test variables."""
        self.dignosis_code = 1
        self.code = Code(dignosis_code=self.dignosis_code, abbreviated_description="new code 1")
    
    def test_model_can_create_a_Code(self):
        old_count = Code.objects.count()
        self.code.save()
        new_count = Code.objects.count()
        self.assertNotEqual(old_count, new_count)
    
    
    

class TestNewCode(TestCase):

    def setUp(self):
        self.code = baker.make('app1.Code')

    def test_model_str(self):
        title = Code.objects.create(title="title test")
        self.assertEqual(str(title), "title test")


class CategoryTest(TestCase):
    """This class defines the test suite for the Category model."""
    
    def setUp(self):
        """Define the test client and other test variables."""
        self.diag_code = "A00"
        self.Category = Category(diag_code=self.diag_code, title="title test")
    
    def test_model_can_create_a_Category(self):
        old_count = Category.objects.count()
        self.Category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)
    
    
    

class TestNewCategory(TestCase):

    def setUp(self):
        self.Category = baker.make('app1.Category')

    def test_model_str(self):
        title = Category.objects.create(title="title test")
        self.assertEqual(str(title), "title test")
