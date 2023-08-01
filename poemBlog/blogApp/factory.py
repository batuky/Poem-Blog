import factory

from django.contrib.auth.models import User

from factory.faker import faker

from .models import Post

FAKE = faker.Faker()

"""
This code generates data for database as posts.

INSTRUCTIONS
1- Open env, change directory to the app directory
2- Write the code into the terminal python manage.py shell
3- Write the code "from blogApp.factory import PostFactory" and enter
4- Write the code "x = PostFactory.create_batch(100)" enter
5- Then exit()
"""

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username ="admin")[0]


    @factory.lazy_attribute
    def content(self):
        x = ""
        for _ in range(0,5):
            x += "\n" + FAKE.paragraph(nb_sentences=30)+"\n"
        return x
    
    status = "published"


