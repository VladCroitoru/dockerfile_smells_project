FROM python:3.7.6-alpine
ENV PYTHONBUFFERED 1
ENV ICMS_WEB_PORT ${ICMS_WEB_PORT}
ENV DOCKERIZE_VERSION v0.6.1
RUN mkdir /code
RUN mkdir /deps
WORKDIR /code
COPY Pipfile Pipfile.lock /code/

# Install dependencies
RUN \
  apk add --no-cache postgresql-libs openssl && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python3 -m pip install --upgrade pip && \
  python3 -m pip install pipenv && \
  python3 -m pipenv install --system --dev --deploy && \
  apk --purge del .build-deps
# Install dockerize
RUN \
  wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz
COPY . /code/
CMD scripts/entry.sh
