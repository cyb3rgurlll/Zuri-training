#Name: Osarenkhoe Chima-Nwogwugwu
#Student id: I4G033993TR5
class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name:str, age:int, tracks:list, score:float):
        #Instance variables
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score

    def change_name(self, new_name):
        self.new_name=new_name
        print("Name: ",new_name)

    def change_age(self, new_age):
        self.new_age=new_age
        print("Age: ",new_age)

    def add_track(self, new_track):
        self.new_track=new_track
        print("Track: ",new_track)

    def get_score(self):
        return self.score

    #Object of Student class
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print("Score: ", Bob.get_score())
