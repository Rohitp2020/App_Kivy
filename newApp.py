##  Kivy is an open source software library for the rapid development of applications equipped with novel user interfaces, such as multi-touch apps.
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout  ## for structure or ui
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):         ## This class used to create grid structure and layout of our app
    def __init__(self,**kwargs):    ## '**kwargs' used for adding lot of method and arguements
        super(childApp,self).__init__()
        self.cols = 2               ## to define columns of our app

        self.add_widget(Label(text='Student_Name'))           ## to define labels
        self.s_name = TextInput()    ## to store student name in a variable
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student_Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='Student_Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.save = Button(text="Firstly, Click here to save your Data.")          ## here we created the click button for saving our data.
        self.save.bind(on_press = self.click_me)
        self.add_widget(self.save)

        self.next = Button(text="Please, Click here for next Entry.")             ## here we created the click button for next entry.
        self.next.bind(on_press= self.nexty)
        self.add_widget(self.next)


    def click_me(self, instance):                     ## here we defined 'click button' functionality
        print("Name of student is: " + self.s_name.text)
        print("Marks of student is: " + self.s_marks.text)
        print("Gender of student is: " + self.s_gender.text)
        print("")

    def nexty(self,instance):
        self.s_name.text = ''
        self.s_marks.text = ''
        self.s_gender.text = ''

class parentApp(App):
    def build(self):        ## 'method' to build an app
        return childApp()


if __name__ == "__main__":  ## to confirm our app run in main function
    parentApp().run()

