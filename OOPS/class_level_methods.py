#when we are delcARING ANY CLAS LEVEL METHODS WE HAVE to use the name of the method as @classmethod
#in classmethod we cannnt use the instance variables
#in class method the reference variable is actually denoted by cls

class Bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print("{} fly with {} wings".format(name,cls.wings))
Bird.fly("parrot")
Bird.fly("Eagle")
