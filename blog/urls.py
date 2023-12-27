from django.urls import path, include

import blog.views

urlpatterns=[
    # 如果路由含有hello_world，則轉發到blog.views.hello_world 記得不用帶()
    path("hello_world", blog.views.hello_world)
]