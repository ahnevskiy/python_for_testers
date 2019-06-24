__author__ = 'ahnevskiy'


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, path_to_photo=None, title=None,
                 company=None, address=None, phone_home=None, phone_mobile=None, email=None, homepage=None,
                 birthday=None, anniversary_day=None, second_address=None, second_phone=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.path_to_photo = path_to_photo
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.email = email
        self.homepage = homepage
        self.birthday = birthday
        self.anniversary_day = anniversary_day
        self.second_address = second_address
        self.second_phone = second_phone
        self.notes = notes
