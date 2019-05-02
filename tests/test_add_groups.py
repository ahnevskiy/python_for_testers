# -*- coding: utf-8 -*-
__author__ = 'ahnevskiy'

from model.group import Group


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


def test_delete_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


def test_edit_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit_first_group(Group(name="Its a new name",
                                     header="New header",
                                     footer="And new footer"))
    app.session.logout()
