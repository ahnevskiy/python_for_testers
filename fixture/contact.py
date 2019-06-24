__author__ = 'ahnevskiy'

from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def fill_contact_forms(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        wd.find_element_by_name("photo").send_keys(contact.path_to_photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday.day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday.month)
        self.change_field_value("byear", contact.birthday.year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day.day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_day.month)
        self.change_field_value("ayear", contact.anniversary_day.year)
        self.change_field_value("address2", contact.second_address)
        self.change_field_value("phone2", contact.second_phone)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_forms(contact)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # check a first contact
        wd.find_element_by_name("selected[]").click()
        # submit contact deleting
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # begin contact editing
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_forms(contact=contact)
        # confirm edit
        wd.find_element_by_xpath("//input[@value='Update']").click()
