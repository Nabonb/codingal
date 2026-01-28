class myClass:
    __privateVar = 27

    def __privMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private Variable value:", myClass.__privateVar)
        # self.__privMeth()  #this will work too


foo = myClass()
foo.hello()
foo.__privMeth
# foo._myClass__privMeth()
