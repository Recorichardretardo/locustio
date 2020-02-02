from locust import HttpLocust, Locust,TaskSet,between,task



class UserBehaviour(TaskSet):
    @task(1)
    def mytask1(l):
        print("I am Logged In")
    @task(2)
    def mytask2(m):
        print("I am Logged Out")

class User(Locust):
    task_set=UserBehaviour
    wait_time = between(5.0, 9.0)


