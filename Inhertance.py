class Parent():
    def __init__(self,lastname,eye_color):
        print 'parent constructor Called'
        self.lastname = lastname
        self.eye_color = eye_color
    def show_info(self):
        print 'LastName : '+self.lastname
        print 'EyeColor : '+self.eye_color


class Child(Parent):
    def __init__(self,lastname,eye_color,number_of_toys):
        print 'Child constructor Called'
        Parent.__init__(self,lastname,eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print 'LastName : ' + self.lastname
        print 'EyeColor : ' + self.eye_color
        print  'number of toys : '+str(self.number_of_toys)
billy_cyrus = Parent("Cyrus",'blue')
#billy_cyrus.show_info()

miley_cyrus = Child('Cyrus',"Blue",5)
#print miley_cyrus.lastname
#print miley_cyrus.number_of_toys
miley_cyrus.show_info()