from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from ..models import Post


class PostVistasTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Aaron', last_name='Bob')
        for x in range(20):
            Post.objects.create(title=f'My first post {x}',
                                slug=f'my-first-post-{x}',
                                author=u,
                                content=f'My first post content {x}')

    def test_urls(self):
        '''
        Comprobar que el listado de posts devuelve 20 posts
        '''
        # Página inicial
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        # Admin
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 302)

        # Primer post
        p = Post.objects.first()
        slug = p.slug
        response = self.client.get(f'/{slug}/')
        self.assertEquals(response.status_code, 200)
