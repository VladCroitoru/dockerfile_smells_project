FROM python:3.7-alpine3.8
ARG packages
RUN apk --update add ${packages} \
    && rm -rf /var/cache/apk/*
RUN pip3 install pipenv

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app

# -- Adding Pipfiles
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
ONBUILD RUN set -ex && pipenv install --deploy --system