import unittest
from extensions import db
from models.blog import Blog
from app import create_app
from config import TestConfig


app = create_app(config_class=TestConfig)
app.config.from_object(TestConfig)
client = app.test_client()


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        ctx = app.app_context()
        ctx.push()
        with client:
            test_blog = Blog(
                title="Testing a Portfolio site",
                url="http://localhost:5000/blog",
                description="This post demonstrates the steps to unit test a Flask application",
            )
            db.create_all()
            db.session.add(test_blog)
            db.session.commit()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()


class TestCases(BaseTestCase):

    # Helper methods
    def contact(self, name, email, subject, message):
        return client.post(
            "/contact",
            data=dict(name=name, email=email, subject=subject, message=message),
        )

    # Test Cases
    def test_home(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Abhishek Pednekar", response.data)  # Test title
        self.assertIn(
            b"https://github.com/AbhishekPednekar84", response.data
        )  # Test social link
        self.assertIn(b"Portfolio", response.data)

    def test_portfolio(self):
        response = client.get("/portfolio")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"BIO", response.data)
        self.assertIn(b"Skills", response.data)
        self.assertIn(b"CodeDisciples.in", response.data)
        self.assertIn(b"Bangalore", response.data)  # Test footer

    def test_blog(self):
        response = client.get("/blog")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Code Disciples", response.data)
        self.assertIn(b"Testing a Portfolio site", response.data)
        self.assertIn(b"http://localhost:5000/blog", response.data)
        self.assertIn(
            b"This post demonstrates the steps to unit test a Flask application",
            response.data,
        )
        self.assertIn(b"Bangalore", response.data)  # Test footer

    def test_invalid_page(self):
        response = client.get("/blog?page=2")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Not Found", response.data)

    def test_contact(self):
        response = client.get("/contact")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Contact Me", response.data)
        self.assertIn(b"References", response.data)
        self.assertIn(b"Bangalore", response.data)  # Test footer

    def test_email_success(self):
        response = self.contact(
            "Test Joe",
            "TestJoe@email.com",
            "Test Subject",
            "This is a test message",
        )

        self.assertTrue(b"Thanks! I will be in touch soon.", response.data)

    def test_email_with_invalid_email(self):
        response = self.contact(
            "Test Joe", "TestJoe", "Test Subject", "This is a test message"
        )
        self.assertTrue(b"Invalid email address.", response.data)

    # def test_search_api_with_id(self):
    #     response = client.get("/api/search/1")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b"Testing a Portfolio site", response.data)

    # def test_search_api_for_all_articles(self):
    #     response = client.get("/api/search_all")
    #     self.assertEqual(response.status_code, 308)
