###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.2 as builder

ENV PYTHONDONTWRITEBYCECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apt-get update -y && apt-get -y install postgresql gcc python3-dev musl-dev

# lint
RUN pip install --upgrade pip

COPY . .

# install dependencies
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9.2

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN groupadd app
RUN useradd -m -g app app -p FAcademy5671313
RUN usermod -aG app app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update \
    && apt-get install netcat -y
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
