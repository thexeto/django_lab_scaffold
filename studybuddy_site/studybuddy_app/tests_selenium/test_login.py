from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth.models import User
# https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#django.contrib.staticfiles.testing.StaticLiveServerTestCase
# https://docs.djangoproject.com/en/4.2/topics/testing/tools/#django.test.LiveServerTestCase

from django.utils import timezone
from django.urls import reverse
from studybuddy_app.models import Meetup
import datetime


def create_meetup(meetup_title, meetup_location="Room 11", days=2):
    start_time = timezone.now() + datetime.timedelta(days=days)
    end_time = start_time + datetime.timedelta(hours=2)
    return Meetup.objects.create(
        title=meetup_title,
        location=meetup_location,
        start_time=start_time,
        end_time=end_time)


class LoginTest(StaticLiveServerTestCase):
    fixtures = ["user.yaml"]  # , "meetup.yaml"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    # https://www.selenium.dev/documentation/webdriver/elements/finders/

    def test_login(self):
        self.selenium.get(f"{self.live_server_url}/accounts/login/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("admin")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("geheim12")
        self.selenium.find_element(
            By.XPATH, '//button[@type="submit"]').click()
        
        body = self.selenium.find_element(By.TAG_NAME, "body")
        failure_text = "Please enter a correct username"
        assert failure_text not in body.text

    def test_failed_login(self):
        self.selenium.get(f"{self.live_server_url}/accounts/login/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("admin")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("incorrect_password")
        self.selenium.find_element(
            By.XPATH, '//button[@type="submit"]').click()
        
        body = self.selenium.find_element(By.TAG_NAME, "body")
        failure_text = "Please enter a correct username"
        assert failure_text in body.text
