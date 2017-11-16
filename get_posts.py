import os

class PostsData:
    headers = {
        'Content-Type': 'application/json'
    }

    @property
    def get_posts(self):
        # post文件位置
        dir_name = 'post_test'

        file_names = os.listdir(dir_name)

        posts = {}
        for file_name in file_names:
            with open('%s/%s' % (dir_name, file_name)) as f:
                posts.update({file_name[:-4]:f.read()})
        # 返回字典类型
        return posts

if __name__ == '__main__':
    post = PostsData()
    print(post.headers)
    print(post.get_posts)