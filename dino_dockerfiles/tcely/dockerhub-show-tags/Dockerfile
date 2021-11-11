FROM tcely/alpine-stable
LABEL maintainer="https://keybase.io/tcely"

RUN apk --update add \
      krb5 python2 py2-cryptography py2-yaml && \
    apk add --virtual .build-pytools \
      build-base git krb5-dev py2-pip python2-dev && \
    git clone --recurse-submodules --single-branch 'https://github.com/HariSekhon/pytools.git' /pytools ; \
    pip install beautifulsoup4 blessings docker requests_kerberos ; \
    apk del --purge .build-pytools ; \
    rm -rf /var/cache/apk/* ; \
    /pytools/dockerhub_show_tags.py alpine

ENTRYPOINT ["/pytools/dockerhub_show_tags.py"]
