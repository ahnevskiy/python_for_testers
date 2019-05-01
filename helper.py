__author__ = 'ahnevskiy'

class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class Contact:
    def __init__(self, firstname, middlename, lastname, nickname, path_to_photo, title, company, address, phone_home,
                 phone_mobile, email, homepage, birthday, anniversary_day, second_address, second_phone, notes):
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


class Date:
    def __init__(self, day, month, year):
        self.day = str(day)
        self.month = convert_mount(month=month)
        self.year = str(year)


def convert_mount(month):
    # converts the month number to a word
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return"May"
    elif month == 6:
        return"June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
