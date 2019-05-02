# -*- coding: utf-8 -*-
__author__ = 'ahnevskiy'

import pytest
from model.objects import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="Its a test group",
                           header="My first group for test",
                           footer="Its a description of this group"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
