# syntax=docker/dockerfile:1


###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.3 as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########
FROM adoptopenjdk/openjdk11:jre-nightly

# create directory for the app user
RUN mkdir -p /home/app

## create the app user
RUN groupadd app && useradd -g app app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

# Install requirements
RUN apt update && apt install -y \
    software-properties-common python3.9 python3-distutils python3-pip python3-apt
RUN pip3 install --no-cache /wheels/*

# copy docker-entrypoint.sh
COPY docker-entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# Expose port
EXPOSE 8000

# Sets the system call signal used to stop the instance
STOPSIGNAL SIGTERM

# Run entrypoint
RUN chmod a+x /home/app/web/docker-entrypoint.sh
ENTRYPOINT [ "sh", "/home/app/web/docker-entrypoint.sh" ]
