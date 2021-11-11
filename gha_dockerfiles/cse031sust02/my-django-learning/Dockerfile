# FROM - Image to start building on.
FROM python:3

# set the environment variable
ENV PYTHONUNBUFFERED=1

# set the working directory
WORKDIR /usr/src/my-django-learning

# install pipenv
RUN pip install -U pipenv

# copy our Pipfile and Pipfile.lock to container
COPY Pipfile Pipfile.lock ./

# install all required packages on the container
RUN pipenv install --system

# copy all files and directories from <src> to <dest>
# <src> = current directory on host machine
# <dest> = filesystem of the container
COPY . .