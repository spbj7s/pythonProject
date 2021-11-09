# class Movie:
#
#     def __init__(self,title,actor,actress):
#         self.title = title
#         self.actor = actor
#         self.actress = actress
#     def info(self):
#         print("Enter the title of the movie: ",self.title)
#         print("Enter the Actor name in the movie: ",self.actor)
#         print("Enter the Actress name in the movie: ",self.actress)
#
# list_of_movies = []
# while True:
#     title = input("enter the title of the movie: ")
#     actor = input("enter the name of the Actor: ")
#     actress = input("enter the name of the actress: ")
#     m =Movie(title, actor, actress)
#     list_of_movies.append(m)
#     print("movies added to the list successfully",list_of_movies)
#     option = input("Do you want to add more movies(Yes/No): ")
#     if option.upper() == "NO":
#         break
# print("this is all the movie list ")
# for movie in list_of_movies:
#     movie.info()
#     print()


class Movie:
    def __init__(self,title,actor,actress):
        self.title=title
        self.actor=actor
        self.actress=actress
    def info(self):
        print("the name of the movie is :",self.title)
        print("the actor name is: ",self.actor)
        print("The actress name is: ",self.actress)
list_movies=[]
while True:
    title=input("Enter the tile of the movie: ")
    actor=input("Enter the actress in the movie: ")
    actress=input("Enter the Actress name is: ")
    m=Movie(title,actor,actress)
    list_movies.append(m)
    print("movie name is successfully adde to the list")
    option=input("Do you want to enter more movies:Yes/No: ")
    if option.lower() == "no":
        break
for movie in list_movies:
    movie.info()
    print()


