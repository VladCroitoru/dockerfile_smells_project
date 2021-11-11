FROM alpine:3.10

RUN apk add --no-cache \
        bash \
        curl \
        openssl \
        python

ARG DEHYDRATED_TAG=v0.6.5
ARG LETSENCRYPT_OVH_HOOK=1800b57991db4357536561a06f82dbfe4f076a2d
RUN apk add --no-cache tar && \
    mkdir dehydrated && \
    curl -L https://github.com/lukas2511/dehydrated/archive/${DEHYDRATED_TAG}.tar.gz | tar -C dehydrated --strip-components 1 -xzf - && \
    mkdir -p dehydrated/hooks/ovh && \
    curl -L https://github.com/Rbeuque74/letsencrypt-ovh-hook/archive/${LETSENCRYPT_OVH_HOOK}.tar.gz | tar -C dehydrated/hooks/ovh --strip-components 1 -xzf - && \
    apk del --no-cache tar

RUN apk add --no-cache py2-pip && \
    pip install --no-cache-dir -r dehydrated/hooks/ovh/requirements.txt && \
    apk del --no-cache py2-pip

RUN mkdir /etc/dehydrated && \
    sed \
        -e 's/#CHALLENGETYPE=.*/CHALLENGETYPE="dns-01"/' \
        -e 's@#HOOK=.*@HOOK=/dehydrated/hooks/ovh/hook.py@' \
        /dehydrated/docs/examples/config > /dehydrated/config

COPY /docker-entrypoint.sh .

ENTRYPOINT [ "/docker-entrypoint.sh" ]

RUN mkdir /var/run/dehydrated

WORKDIR /var/run/dehydrated

