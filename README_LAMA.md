# To create a new project from a cloned repository:
- Opened PycharmProjects and made sure it does not have .git and venv file
- inside this directory in the terminal made git clone the tdd repo
- from the file chose new project chose the location to be the repo tdd-class---> create project from existing 
this created a clean virtual environment which is activated in the terminal

# some changes to the requirements
- Deleted Ww from line 2 in the requirements
- added pydantic to the requirement
- installed requirement plugin
- the requirement file will check if some requirements are not satisfied and ask to install them
- installed tox and from the tox.ini file deleted --basement="{environment}" {postgres} from line 15
- jwd
- bcrypt
- PyJWD

# to go to the fastapi version 
run: 
```commandline
git fetch --tags
git checkout tags/v0.1-fastapi -b fastapi-latest-version
```

# to get a branch which is in the remote to your machine:

```commandline
git pull
git checkout branch_name
git pull
```

# to save your working directory when you are not ready to commit and want to switch the branch then 
```commandline
git stash
git checkout new_branch
# If you only had a look on there and did not want to save chenges then switch back to your branch
git checkout first_branch
git stash pop
```

If you want to save the changes in the new branch too then stash there and use the git stash tool from the pycharm menu
# to push a new branch to the remote for the first time:
```commandline
git push -u origin another_trial_models
```


# to search a ModelViewSet using a method (via queryset and filter)

check the search results in the browser
`http://localhost:8000/posts/?search_terms=value`\
e.g. ```http://127.0.0.1:8000/posts/?search_terms=La```

to search inside the list of a specific user localhost/books/?search_terms=python&author=mathias

```python
from posts.serializers import *
from user_mgmt.models import *
from rest_framework.viewsets import ModelViewSet

class PostViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.query_params.get('search_terms')#localhost/books/?search_terms=python&author=mathias
        if search_term:
            queryset = Post.objects.filter(title__contains=search_term)
        else:
            queryset = Post.objects.all()
        return queryset
```
# work with models in the shell

```django- shell

from posts.models import *
from user_mgmt.models import *
BaseUser.objects.all()
BaseUser.objects.first()
Post.objects.all()
Post.objects.first()


```
# Work with serializers in the shell

You're getting this error as the HyperlinkedIdentityField expects to receive request in context of the serializer so it can build absolute URLs. As you are initializing your serializer on the command line, you don't have access to request and so receive an error.

If you need to check your serializer on the command line, you'd need to do something like this:
````python
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from user_mgmt.serializers import *

factory = APIRequestFactory(SERVER_NAME='localhost')
request = factory.get('/')


serializer_context = {
    'request': Request(request),
}

p = BaseUser.objects.first()
s = BaseUserSerializer(instance=p, context=serializer_context)

print s.data
````
# Old code for filtering posts by students, teachers, and institutions

```python
from posts.serializers import *
from user_mgmt.models import *
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        search_key = list(self.request.query_params.keys())
        if not search_key:
            return queryset
        elif search_key[0] == 'posts_by':
            search_term = self.request.query_params.get(search_key[0])

            if search_term == "students":
                Student_ids = Student.objects.values_list('baseuser_ptr_id')
                queryset = Post.objects.filter(creator__id__in=Student_ids)
            elif search_term == "teachers":
                Teacher_ids = Teacher.objects.values_list('baseuser_ptr_id')
                queryset = Post.objects.filter(creator__id__in=Teacher_ids)
            elif search_term == "institutions":  #
                Institution_ids = Institution.objects.values_list('baseuser_ptr_id')
                queryset = Post.objects.filter(creator__id__in=Institution_ids)

            else:
                queryset = []  # Post.objects.all()

            return queryset

```
# studentposts view trial
```python
class StudentPosts(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        student_ids = Student.objects.values_list('baseuser_ptr_id')
        student_posts = Post.objects.filter(creator__id__in=student_ids)
        serializer = PostSerializer(student_posts, many=True, context={'request': request})
        return Response({"student_posts": serializer.data}, template_name='posts/posts_by_students.html')

```
# posts from a specific user
```python
class UserPostListView(APIView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    # renderer_classes = [TemplateHTMLRenderer]

    @staticmethod
    def get(request, username):
        user = get_object_or_404(BaseUser, username=username) # username should be required
        user_posts = Post.objects.filter(creator=user).order_by('created_at')
        serializer = PostSerializer(user_posts, many=True, context={'request': request})
        return Response({"user_posts": serializer.data}, template_name='posts/user_posts.html')
        # return JsonResponse({"user":serializer.data})
```

and the url will be 
```python
path('posts/user/username=<str:username>', UserPostListView.as_view(), name='user-posts'),
    # posts by specific user (where username should be unique or it needs to be searched by first and last name
    # path(r'^post/user/(?P<username>\d+)/$/', UserPostListView.as_view(), name='user-posts'),
    # path(r'^(?P<username>\d+)/$/', UserPostListView.as_view(), name='user-posts'),
```