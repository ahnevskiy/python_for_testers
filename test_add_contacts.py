# -*- coding: utf-8 -*-
__author__ = 'ahnevskiy'

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from helper import Contact
from helper import Date


class test_add_contacts(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, user_name, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, contact):
        wd = self.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact forms
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # wd.find_element_by_name("photo").send_keys("C:\\Users\\VanteyN\\Pictures\\sample.jpg")
        wd.find_element_by_name("photo").send_keys(contact.path_to_photo)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday.day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday.month)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday.year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day.day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_day.month)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_day.year)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.second_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.second_phone)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        self.login(user_name="admin", password="secret")
        sample_contact = Contact(firstname="Pupkin",
                                 middlename="Petrovich",
                                 lastname="Vasiliy",
                                 nickname="PupOk",
                                 path_to_photo="C:\\sample.jpg",
                                 title="Indian",
                                 company="SVJ",
                                 address="Moscow, Bronnaya, 15",
                                 phone_home="+7(495)123-45-67",
                                 phone_mobile="+7(903)111-22-33",
                                 email="pupkin89@post.ru",
                                 homepage="vk.com/vaska",
                                 birthday=Date(day=15,
                                               month=11,
                                               year=1989),
                                 anniversary_day=Date(day=16,
                                                      month=10,
                                                      year=2015),
                                 second_address="Krasnogorsk, Bridge st, 19",
                                 second_phone="+7(499)222-33-44",
                                 notes="I have never been there")
        self.create_contact(sample_contact)
        self.logout()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
