FROM jouve/poetry:1.1.10-alpine3.14.2

COPY pyproject.toml poetry.lock /srv/

WORKDIR /srv

RUN poetry export --without-hashes > /requirements.txt

FROM alpine:3.14.2

COPY --from=0 /requirements.txt /usr/share/pgadmin4/requirements.txt

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
        gcc \
        g++ \
        libffi-dev \
        make \
        musl-dev \
        postgresql-dev \
        python3-dev \
        ssmtp \
    ; \
    python3 -m venv /usr/share/pgadmin4; \
    /usr/share/pgadmin4/bin/pip install pip==21.2.4 wheel==0.37.0; \
    /usr/share/pgadmin4/bin/pip install -r /usr/share/pgadmin4/requirements.txt; \
    find /usr/share/pgadmin4/lib/python3.8/site-packages/pgadmin4/docs/en_US -mindepth 1 -maxdepth 1 ! -name _build | xargs rm -rf; \
    apk add --no-cache --virtual .run-deps postgresql-client python3 $( \
        scanelf --needed --nobanner --format '%n#p' --recursive /usr/share/pgadmin4 \
        | tr ',' '\n' \
        | sed 's/^/so:/' \
        | sort -u \
        | grep -v libgcc_s \
    ); \
    apk del --no-cache .build-deps; \
    rm -rf /root/.cache /root/.cargo

COPY entrypoint.sh /usr/bin

EXPOSE 80
EXPOSE 443
VOLUME /var/lib/pgadmin

CMD ["entrypoint.sh"]
