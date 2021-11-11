FROM alpine:edge

LABEL Maintainer="Jean-Paul Duyx | github.com/jpduyx" \
      Description="Lightweight ansible container as drone.io plugin with apache_libcloud based on Alpine Linux."

# Install packages

RUN apk add --no-cache ansible openssh-client  && \
      python3 -m ensurepip && \
      pip3 install --no-cache-dir docker apache_libcloud google-auth requests  && \
      rm -rf /usr/bin/pip3* && \
      rm -rf /usr/lib/python*/ensurepip && \ 
      rm -rf /root/.cache && \
      rm -rf /tmp/* && \
      rm -rf /var/cache/apk/*

ENV PATH /usr/sbin:$PATH

CMD ["ansible-playbook"]
