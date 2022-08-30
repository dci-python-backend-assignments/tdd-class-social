# Class Social App

Welcome team! It is very good to have you here to start our new project, the Class Social. The Class Social project
is intended to connect students worldwide, allowing them to share classroom and campi experiences. This is the
starting point of our development journey.

## About the App

The Class Social is a catalog of students, educational institutions, and their relationships. Students will use the
platform to share their experiences primarily in the form of posts. Students can connect to other students and
teachers/mentors/professors forming a social network.

Institutions must have a space, a sort of page where they can keep updated information about the institution, offered
courses, labs, and any kind of resources. Also, companies can register themselves in the system to provide internship
positions.

Reviews are also very important in the platform. Students can review institutions and companies that offer internships,
and this will help students decide which career to follow and which university, school, or high school to choose.

One important aspect of the platform is the student exchange section. Students must be able to find institutions that
accept exchange students and read about their programs and how to get funding.

Last, students must be able to share information about available flat shares and dormitories.

Well, these are the main features we foresee now for our Class Social app. Let's move forward and implement it.

## Development Practices

To implement our App, we will adopt some principles, processes, and tools, and you need to stick to them during the
development. Changes can occur and new tools and processes can be introduced, we will start with the following:

- TDD - Test-Driven Development.
- MVC-Like pattern.
  - Routes making the role of views;
  - Controllers holding the business logic;
  - Models to represent database entities;
- Git to version Control.
- GitHub for project management.
- Agile development with Scrum, or sort of! :)

With these tools and our teamwork, we expect to deliver high-quality software that will change students' lives
worldwide.

## Frameworks and Tools

For this project, we are going to use the following tools and languages:

- Python is the main programming language.
- Pytest as the test framework.
- Django Rest Framework for the HTTP API.
- Git for version control.
- GitHub for remote repository and project management.


## Development Process

## GitFlow

We will use the GitFlow Workflow for working with Git. The basic principle is:

> Create a new branch for every new work you will implement - do not commit to the main branch!

After your implementation is done, push your branch to the remote, a GitHub Pull Request will be created, and a review
process of the code will take place. If everything is ok, the code is then merged into the main branch.

The commands you will use more often are:

- git add
- git commit
- git checkout -b new_branch
- git push -u origin new_branch

The last command must be used when you are finished with your work and wants a pull request to be created, remember
the pull request is the process of review of your code.

## TDD

The system MUST be developed using TDD. A test must be the starting point of your code. You are not allowed to start
coding functionality without the proper test. With that in mind, first, create a test that fails, then implement the
code to make the test pass, and refactor your code.

## Scrum

The source of todo tasks is a GitHub project ([link...](https://github.com/orgs/dci-python-backend-assignments/projects/1/views/1)).
We will follow the scrum methodologies, all the task, also known as **stories** in Scrum, are short description of a
functionality to be implemented. Stories *per se* holds the basic details of the feature, sometimes you will think it is
necessary to contact the client to get more details, stories in Scrum can be seen as reminder to talk with the client,
however if you fell you can deliver the feature without a conversation, go ahead.

At the end of each Sprint the client will do a validation test on the features implemented, if something need to be
changed or added a new story will be generated for the next sprint. Your task is to choose a story to implement in the
next Sprint round. Each team member will then give a score for this task, based on how difficult it is, a mean will be 
calculated and this will be the "story points", this can be used later to calculate the velocity of the team, 
that means, how fast the team can progress.

#### The Story Board

We catalog the stories in what we call a Backlog. At each sprint we select some stories to implement. This mechanics is
reflected in what we call a story board. Stories selected in the Backlog goes to the Todo column, then the sprint
begins. As soon as you start to code the story you move the task to the "In progress..." column and when it is done, 
move it to done. All the tasks mut be done at the end of the Sprint.

#### User Stories Workshop

The User Story Workshop is intended to identify the requirements of the system and the features to be implemented,
to define the stories we are going to hold a User Story Workshop with the product owner, a few developers and 
stakeholders. Some objectives of this workshop are:

- Identify the different kinds of users of the system,
- Identify required functionalities,
- Prioritize the stories,
- and share knowledge

### Ways to deploy to Heroku

1. Create `runtime.txt` file in the main directory(tdd-class-social) if it is missing, update it with Python version that is supported by Heroku.

```python-3.10.6```

2. Create a `Procfile` file in the main directory(tdd-class-social) if it is missing. Add the following in the file.

```web: gunicorn <Name of django Project>.wsgi```

3. Make sure to install the heroku toolbelt. Visit https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli
In Linux, (Note: Install it once in your system)

```commandline
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

4. Add the `requirements.txt` file in the main directory(tdd-class-social) if it is missing.

5. Install the following dependencies:

- whitenoise
- gunicorn
- psycopg2-binary
- dj-database-url

This should also be added to your `requirements.txt` file with the versions.

6. Run the command `heroku login` which redirects to the heroku website to create or login to your account.

7. To create Heroku app for the first time type the following command:

```commandline
heroku create
```

8. Make adjustments to your ```settings.py``` file.
Import from dj_database using the following python statement:

```import dj_database_url```

Add the following statements after the `DATABASES` dictionary:

```
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
```

Add the following statement:

```STATIC_ROOT = BASE_DIR / 'app/public/static'```

else run the following command in the terminal:

```commandline
heroku config:set DISABLE_COLLECTSTATIC=1
```

Add the provided heroku domain to the `ALLOWED_HOSTS` list.

Eg: `ALLOWED_HOSTS = ['<.....herokuapp.com>',  '0.0.0.0']`

Add the following the `MIDDLEWARE` list:

```
MIDDLEWARE = [
    ...
    ...
    ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```

9. Push the code to heroku by using the following command:

```commandline
git push heroku main
```

10. If your Django Project has any migrations, run them using the following command:

```commandline
heroku run python manage.py migrate
```

11. If you want to test locally, run the following command:

```commandline
heroku local web
```

12. To test the deployment in heroku, click the ' <https:....herokuapp.com/> deployed to heroku' or run `heroku open`.