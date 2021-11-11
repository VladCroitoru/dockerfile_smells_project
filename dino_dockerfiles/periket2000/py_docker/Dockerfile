# Image for running git projects in python
#
FROM alpine:3.4

# Installing python 
#
RUN echo " ... installing python and git ..." \
#    && apk update \
#    && apk add python \
#    && apk add py-pip \
#    && pip install --upgrade pip
#
    && apk add --no-cache python3 \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools \
    && pip3 install virtualenv \
    && apk --update add git build-base \
    && rm -r /root/.cache \
    && ln -s /usr/bin/python3 /usr/bin/python

ENV PROJECT_DIR /usr/local/pyenv
RUN mkdir -p ${PROJECT_DIR}

COPY init.sh ${PROJECT_DIR}/init-container.sh
COPY env.sh ${PROJECT_DIR}/env.sh
COPY scripts/* ${PROJECT_DIR}/

RUN adduser -S py-user -u 1000 \
    && addgroup -S py-user -g 1000 \
    && chown py-user:py-user ${PROJECT_DIR} \
    && chown py-user:py-user ${PROJECT_DIR}/*.sh \
    && chown -R py-user:py-user /usr/lib/python* \
    && chmod +x ${PROJECT_DIR}/*.sh

USER py-user
ENTRYPOINT ${PROJECT_DIR}/init-container.sh
