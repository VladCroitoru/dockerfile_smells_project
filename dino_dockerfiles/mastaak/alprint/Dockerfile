FROM schmich/armv7hf-alpine-qemu:3.5
MAINTAINER MastaaK

RUN ["cross-build-start"]
RUN addgroup -S user -g 3000 && \
adduser -S user user -u 3000 && \
addgroup user tty  && \
addgroup user dialout && \
apk update && \
  apk add --no-cache python yaml-dev py-setuptools && \
  apk add --no-cache --virtual .build &&\
  apk add git linux-headers gcc libc-dev python-dev py-setuptools python2 py-pip && \
mkdir -p /home/user/octoprint && \
git clone https://github.com/foosel/OctoPrint.git /home/user/octoprint && \
cd /home/user/octoprint && \
pip install --upgrade pip && \
pip install -r requirements.txt --no-cache-dir && \
python setup.py install && \
mkdir /home/user/.octoprint && \
chown -R user:user /home/user/.octoprint &&\
apk del .build && \
rm -rf /home/user/octoprint /root/.cache /var/cache/apk/*
RUN ["cross-build-end"]

USER user
EXPOSE 5000
ENTRYPOINT ["/usr/bin/octoprint"] 
