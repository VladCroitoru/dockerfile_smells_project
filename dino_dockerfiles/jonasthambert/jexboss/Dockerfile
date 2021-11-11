FROM alpine:latest

LABEL maintainer="jonas@thambert.com"

WORKDIR "/root"

RUN  apk add --no-cache python py2-pip git && \
  git clone https://github.com/joaomatosf/jexboss.git && \
  pip install -r jexboss/requires.txt

ENTRYPOINT ["python2.7", "/root/jexboss/jexboss.py"]
