# -*- coding: utf-8 -*-
__author__ = 'ahnevskiy'

from model.contact import Contact
from model.useful import Date


def test_add_contact(app):
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
    app.contact.create(sample_contact)


def test_delete_first_contact(app):
    app.contact.delete_first_contact()


def test_edit_first_contact(app):
    new_contact = Contact(firstname="Rodriguez",
                          middlename="Bending",
                          lastname="Bender",
                          nickname="Bending Unit 22",
                          path_to_photo="C:\\bender.jpg",
                          title="serial number 2716057",
                          company="Planet Express",
                          address="Hostel of robots, room 1001110111001",
                          phone_home="+7(777)777-77-77",
                          phone_mobile="01001010010011101",
                          email="ilovecooking@sexmachine.org",
                          homepage="bender-club.livejournal.com",
                          birthday=Date(day=21,
                                        month=12,
                                        year=2993),
                          anniversary_day=Date(day=1,
                                               month=1,
                                               year=3000),
                          second_address="Wongs farm",
                          second_phone="1001010001000110",
                          notes="kill all humans")
    app.contact.modify_first_contact(new_contact)
