#http://newtours.demoaut.com/login.php
''' action: process
userName: reco.richard
password: J@Nfirst1234
login.x: 0
login.y: 0 '''


from locust import HttpLocust,TaskSet,between,task

class UserBehaviour(TaskSet):

    @task
    def login_post(self):
        print("===========================")
        resp = self.client.post("/login.php",
                                {"action": "process", "userName": "reco.richard", "password": "J@Nfirst1234",
                                 "login.x": "0", "login.y": "0"})
        print(resp.status_code)
        print(resp.headers)
        print(resp.request.headers)
        print("=====================")
        print(resp.text)



class User(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(5.0, 10.0)
    host = "http://newtours.demoaut.com"