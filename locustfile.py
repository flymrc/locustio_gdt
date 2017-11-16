from random import choice
from locust import HttpLocust, TaskSet, task
from get_posts import PostsData


class MyTaskSet(TaskSet):
    def __init__(self, parent):
        TaskSet.__init__(self, parent)
        # 获得请求所需参数实例
        posts_data = PostsData()

        self.headers = posts_data.headers
        # 字典类型
        self.posts = posts_data.get_posts
        # API接口地址
        self.url = '/jsonrpc'

    @task
    def my_task(self):
        print("Locust instance (%r) executing my_task" % (self.locust))
        data = choice(list(self.posts.values()))
        response = self.client.post(self.url, data=data, headers=self.headers)
        print(response.status_code)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000

