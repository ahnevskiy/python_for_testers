# -*- coding: utf-8 -*-
__author__ = 'ahnevskiy'

import pytest
from helper import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="Its a test group",
                                header="My first group for test",
                                footer="Its a description of this group"))
    app.logout()


def test_add_empty_group(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()





