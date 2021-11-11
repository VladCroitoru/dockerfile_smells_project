FROM python:3.9-alpine3.13

RUN pip install --upgrade pip
ADD ./requirements.txt /requirements.txt

# Build dependencies
RUN apk add --no-cache --virtual .build-deps build-base linux-headers gcc \
    musl-dev && apk add --no-cache git && pip install -r /requirements.txt && \
    apk --purge del .build-deps && rm requirements.txt

ADD ./ /app
WORKDIR /app
ENV PYTHONPATH /app

# Track releases in Sentry
ARG CI_COMMIT_ID

# Add a non-root, system user (-S option) to run the application.
# Don't assign a home dir (-H) or set a password (-D).
RUN adduser -SDH -u 1000 home
USER home
