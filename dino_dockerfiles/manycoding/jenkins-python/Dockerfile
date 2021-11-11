FROM jenkins/jenkins:lts-alpine
MAINTAINER Valery M. <manycoding@users.noreply.github.com>

USER root

RUN apk add --no-cache python3 python3-dev curl gcc g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

COPY requirements.txt /server_requirements.txt
RUN pip install -U pipenv && \
    pip install --extra-index-url=https://pypi.python.org/simple/ --no-cache-dir -r /server_requirements.txt

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

USER jenkins
