class Contact:
    def __init__(self, name, phone_number, e_mail, address):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.address = address

    def print_info(self):
        print("name:", self.name)
        print("Phone Number", self.phone_number)
        print("E-mail", self.e_mail)
        print("Address", self.address)


def run():
    kim = Contact('홍길동', '010-6752-2425', 'hw2425@columbia.edu', 'New York')
    kim.print_info()

if __name__ == '__main__':
    run()
