# Class Social App

Welcome team! It is very good to have you here to start our new project, the Class Social. The Class Social project
is intended to connect students all over the world allowing then to share classroom and campi experiences. This is the
starting point of our development journey.

## Development Practices

To implement our App we are will adopt some principles, processes and tools, and you need to stick to them during the 
development. Changes can occur and new tools and processes introduced, we will start with the following:

- TDD - Test-Driven Development.
- MVC-Like pattern.
  - Routes making the role of views;
  - Controllers holding the business logic;
  - Models to represent database entities;
- Git to version Control.
- GitHub for project management.
- Agile development with Scrum, or sort of! :)

With these tools and our teamwork we expect to deliver a high quality software that will change the life of students
around the world.

## Frameworks and Tools

For this project we are going to use the following tools and languages:

- Python as the main programming language.
- Pytest as the test framework.
- FasAPI for the HTTP API.
  - FastAPI uses pydantic for input validation, so the models MUST be writen as Pydantic models.
- Git for version control.
- GitHub for remote repository and project management.


## Development Process

## TDD

The system MUST be developed using TDD, a test is the starting point of your code, you are not allowed to start coding
a functionality without the proper test. With that in mind, first create a test that fails, them implement the code to
make the test pass, refactor your code.

### Scrum

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