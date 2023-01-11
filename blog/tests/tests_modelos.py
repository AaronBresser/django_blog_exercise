from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from ..models import Post, Comment


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Aaron', last_name='Bob')
        p = Post.objects.create(title='My first post',
                                slug='my-first-post',
                                author=u,
                                content='My first post content')
        Comment.objects.create(
            post=p,
            name='Aaron',
            email='aaron.indepediente@hotmail.com',
            body='My first comment'
        )

    def test_metodo_str(self):
        '''
        Comprobar que el print del objeto devuelve su título
        '''
        post = Post.objects.get()
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, str(post))

    def test_slug(self):
        '''
        Comprobar que el slug se crea correctamente
        '''
        post = Post.objects.first()
        slug = post.slug
        expected_slug = post.title.lower().replace(' ', '-')
        self.assertEqual(expected_slug, slug)

    def test_str_comentario(self):
        c = Comment.objects.first()
        expected_object_name = f'Comment {c.body} by {c.name}'
        self.assertEqual(expected_object_name, str(c))
