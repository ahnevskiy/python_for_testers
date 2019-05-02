# -*- coding: utf-8 -*-
__author__ = 'ahnevskiy'

import pytest
from helper import Contact
from helper import Date
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(user_name="admin", password="secret")
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
    app.create_contact(sample_contact)
    app.logout()
