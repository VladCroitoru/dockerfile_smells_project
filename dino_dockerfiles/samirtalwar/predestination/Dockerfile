FROM python:3

RUN set -ex; \
    apt-get update -qq; \
    apt-get upgrade -qqy

RUN apt-get install -qqy zsh

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . ./

CMD ["./web"]
