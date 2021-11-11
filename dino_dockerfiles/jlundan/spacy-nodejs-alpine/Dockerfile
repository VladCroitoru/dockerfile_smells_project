FROM node:8.5.0-alpine

ARG SPACY_VERSION

ENV LANG en
ENV PORT 3000
ENV SPACY_LOG_LEVEL error

COPY ./src /app
COPY ./entry/services.yml /services.yml
COPY ./entry/.bashrc /root/.bashrc

RUN apk update && apk add --no-cache python3 tini bash libgomp && \
    apk add --no-cache --virtual .build-deps \
        build-base \
        subversion \
        python3-dev \
        g++ && \

    ln -s /usr/bin/python3 /usr/bin/python && \

    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \

    python3 -m pip install -U socketIO-client spacy==${SPACY_VERSION} && \
    python3 -m spacy.${LANG}.download && \
    pip show spacy > /etc/spacy_info && \

    npm install --loglevel=warn npm@4.6.1 -global && \

    npm install --loglevel=warn pm2 -g && \
    cd /app && \
    npm install --loglevel=warn && \

    # `nohup node bin/spacy >/dev/null 2>/dev/null &` && \
    # sleep 5 && \
    # npm test && \
    npm prune --production && \

    apk del .build-deps \
        build-base \
        subversion \
        python3-dev \
        g++ && \

    rm -r /usr/lib/python*/ensurepip && \
    rm -r /root/.cache && \
    rm -r /root/.npm

EXPOSE ${PORT}

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["pm2-docker", "/services.yml"]
