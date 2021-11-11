FROM python:2-alpine

ENV VERSION=0.1.21 \
    PACKAGES_FOR_BUILD="gcc musl-dev libffi-dev openssl-dev"

# ElastAlert installation
RUN apk add --no-cache ${PACKAGES_FOR_BUILD} ca-certificates &&\
    pip install elastalert==${VERSION} &&\
    apk del ${PACKAGES_FOR_BUILD} &&\
    rm -rf /root/.cache

CMD elastalert-create-index --config /config.yml --index elastalert_status --old-index '' &&\
    elastalert --config /config.yml
