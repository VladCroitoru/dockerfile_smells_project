FROM registry.gitlab.com/geo-bl-ch/docker/python:alpine-3.14 AS builder

USER 0

RUN apk --update add \
        bash \
        bash-completion \
        shadow \
        build-base \
        nodejs \
        npm \
        uwsgi-python3 \
        python3-dev \
        libffi-dev

COPY . /app

WORKDIR /app

RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install wheel && \
    .venv/bin/pip install pyyaml && \
    .venv/bin/pip install -e . && \
    npm install && \
    ./node_modules/.bin/webpack

USER 1001

FROM registry.gitlab.com/geo-bl-ch/docker/python:alpine-3.14

USER 0

RUN apk --update add \
        bash \
        uwsgi-python3 \
        libffi

COPY --from=builder --chown=1001:0 /app/.venv /app/.venv
COPY --from=builder --chown=1001:0 /app/oereb_client/*.py /app/oereb_client/
COPY --from=builder --chown=1001:0 /app/oereb_client/templates /app/oereb_client/templates
COPY --from=builder --chown=1001:0 /app/oereb_client/views /app/oereb_client/views
COPY --from=builder --chown=1001:0 /app/oereb_client/static/i18n /app/oereb_client/static/i18n
COPY --from=builder --chown=1001:0 /app/oereb_client/static/images /app/oereb_client/static/images
COPY --from=builder --chown=1001:0 /app/oereb_client/static/build /app/oereb_client/static/build
COPY --from=builder --chown=1001:0 /app/oereb_client.egg-info /app/oereb_client.egg-info
COPY --from=builder --chown=1001:0 /app/app.ini /app/app.ini

ENV PATH="/app/.local/bin:${PATH}"

EXPOSE 8080

USER 1001

CMD ["uwsgi", "--plugin", "python3", "--http-socket", "0.0.0.0:8080", "--ini-paste-logged", "/app/app.ini"]
