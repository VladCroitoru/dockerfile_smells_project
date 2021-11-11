FROM python:2.7

COPY . /usr/local/src/cloudflare-stun

WORKDIR /usr/local/src/cloudflare-stun

RUN python setup.py install

ENTRYPOINT ["/usr/local/src/cloudflare-stun/bin/entrypoint.sh"]
