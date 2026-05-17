from django.test import TestCase
from django.urls import reverse


class PortfolioPageTests(TestCase):
    def test_home_page_renders_student_context(self):
        response = self.client.get(reverse("base:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ravi Ranjan Kashyap")
        self.assertContains(response, "Keep Practicing!")
        self.assertContains(response, "E-Commerce Website")

    def test_about_page_renders_profile_details(self):
        response = self.client.get(reverse("base:about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lovely Professional University")
        self.assertContains(response, "Career Goals")
        self.assertContains(response, "Creative Skills")

    def test_contact_endpoint_accepts_valid_submission(self):
        response = self.client.post(
            reverse("base:contact"),
            {
                "name": "Portfolio Reviewer",
                "email": "reviewer@example.com",
                "message": "Great work.",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {"ok": True, "message": "Thanks, Ravi received your message draft successfully."},
        )

    def test_contact_endpoint_rejects_missing_fields(self):
        response = self.client.post(reverse("base:contact"), {"name": "Portfolio Reviewer"})

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(
            response.content,
            {"ok": False, "message": "Please complete all required fields."},
        )
