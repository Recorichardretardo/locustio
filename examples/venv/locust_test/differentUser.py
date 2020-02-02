#http://newtours.demoaut.com/login.php
''' action: process

login.x: 0
login.y: 0 '''

from locust import HttpLocust,TaskSet,between,task

userName = [
    ("qamile1@gmail.com","qamile"),
    ("qamile2@gmail.com", "qamile"),
    ("qamile3@gmail.com", "qamile"),
    ("qamile4@gmail.com", "qamile"),
    ("qamile5@gmail.com", "qamile")
]

class UserBehaviour(TaskSet):

    def on_start(self):
        self.userName = "Not_exist"
        self.password = "Not_exist"
        if len(userName)>0:
            self.userName,self.password = userName.pop()
    @task
    def login_post(self):
        print(self.userName)
        self.client.post("/login.php",
                                {"action": "process", "userName": self.userName, "password": self.password,
                                 "login.x": "16", "login.y": "9"})

class User(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(5.0, 10.0)
    host = "http://newtours.demoaut.com"