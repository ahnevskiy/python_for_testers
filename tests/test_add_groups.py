# -*- coding: utf-8 -*-
__author__ = 'ahnevskiy'

from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Its a test group",
                           header="My first group for test",
                           footer="Its a description of this group"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) + 1


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group())
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) + 1


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) - 1



def test_modify_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="Its a new name",
                                       header="New header",
                                       footer="And new footer"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)

