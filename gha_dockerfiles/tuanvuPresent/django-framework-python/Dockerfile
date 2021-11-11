#FROM python:3
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
#WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#COPY . /code/


FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
RUN mkdir /usr/src/app/logs
