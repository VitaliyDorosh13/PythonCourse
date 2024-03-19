'''When we define a method, we do so using def, followed by the name of the method.
Methods contain arguments, encapsulated in parentheses. Every method of a class
must contain the self argument at the very least; they can contain any number of other
arguments as well (more on this soon!).
self is used to reference the instance of the object you create. Again, this will make
more sense as we actually create our classes and put them to work.'''

class Superhero():
    def fly(self):
        print("Look at me, i'm so fly!")
    
    def hotDog(self):
        print("I sure do like hot dogs!")

HotDogMan = Superhero()
HotDogMan.fly()
HotDogMan.hotDog()

