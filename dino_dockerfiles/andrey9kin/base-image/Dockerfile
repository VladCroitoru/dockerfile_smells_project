FROM alpine:3.5

# Support for proxies.
# Values should be passed as build args
# http://docs.docker.com/engine/reference/builder/#arg
ENV http_proxy ${http_proxy:-}
ENV https_proxy ${https_proxy:-}
ENV no_proxy ${no_proxy:-}

# Install dump init
# Read more here https://github.com/Yelp/dumb-init
ENV DUMB_INIT_VER=1.2.0
RUN apk add --no-cache --virtual .tmp-packeges python2 python2-dev py2-pip build-base \
    && echo "dumb-init==1.2.0 --hash sha256:51274b5f8d82846e959b96605a3213eddc462bcb3eaec3bc4ec0b1df5ab14e6d" > requirements.txt \
    && pip install --require-hash -r requirements.txt\
    && apk del .tmp-packeges \
    && rm -f requirements.txt

# Install openssl to allow downloads over https
# Intentially using latest version
RUN apk add --no-cache openssl

ENTRYPOINT ["dumb-init"]
CMD ["/bin/sh"]
