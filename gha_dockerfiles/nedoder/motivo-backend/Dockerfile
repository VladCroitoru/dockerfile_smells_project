FROM python:3.9-slim-buster as base

ENV APP_HOME=/code
ENV APP_USER=user

WORKDIR $APP_HOME

ENV TZ 'Europe/Warsaw'

RUN echo $TZ > /etc/timezone && apt-get update && \
    apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get install -y xfonts-75dpi xfonts-base wget libpq-dev gcc

RUN pip install --upgrade pip

FROM base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY app/requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

EXPOSE 8000

# STOPSIGNAL SIGINT

# Copy project code.
COPY ./app/ /code/

# RUN useradd $APP_USER

# RUN chown -R $APP_USER:$APP_USER $APP_HOME
# USER $APP_USER

WORKDIR /code
