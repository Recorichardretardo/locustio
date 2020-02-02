from locust import HttpLocust,TaskSet,between,task

class UserBehaviour(TaskSet):
    @task
    def launch_url(self):
        self.client.get("/")

class User(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(5.0, 9.0)
    host = "http://newtours.demoaut.com"
    # we can give from command prompt also
    # locust -f locust_http_get.py --web-port 8083 --host="http://newtours.demoaut.com"
    # host = "http://newtours.demoaut.com"