# -*- coding: utf-8 -*-
__author__ = 'ahnevskiy'

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Its a test group",
                           header="My first group for test",
                           footer="Its a description of this group"))


def test_add_empty_group(app):
    app.group.create(Group(name=None, header=None, footer=None))


def test_delete_first_group(app):
    app.group.delete_first_group()


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="Its a new name",
                                       header="New header",
                                       footer="And new footer"))
