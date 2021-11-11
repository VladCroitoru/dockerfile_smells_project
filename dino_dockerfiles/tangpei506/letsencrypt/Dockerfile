FROM alpine:3.3

# Install letsencrypt, code forked from https://github.com/xataz/dockerfiles/blob/master/letsencrypt/Dockerfile
# replace letsencrypt-auto with acme-tiny

WORKDIR /acme-tiny
ENV PATH /acme-tiny/venv/bin:$PATH

RUN export BUILD_DEPS="git \
                build-base \
                libffi-dev \
                linux-headers \
                openssl-dev \
                py-pip \
                python-dev" \
    && apk add -U dialog \
                python \
                curl \
                bash \
                augeas-libs \
                openssl \
                ${BUILD_DEPS} \
    && pip --no-cache-dir install virtualenv \
    && git clone https://github.com/tangpei506/acme-tiny.git /acme-tiny \
    && git checkout patch-1 \
    && virtualenv --no-site-packages -p python2 /acme-tiny/venv \
    && /acme-tiny/venv/bin/pip install -r /acme-tiny/tests/requirements.txt \
    && apk del ${BUILD_DEPS} \
    && rm -rf /var/cache/apk/*
    
ADD get_cert.sh /acme-tiny/
RUN chmod +x get_cert.sh

ENTRYPOINT ["/acme-tiny/get_cert.sh"]
