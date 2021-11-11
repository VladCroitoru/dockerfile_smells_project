FROM alpine:3.4

COPY .bashrc .inputrc /root/

RUN set -x \
	&& apk add --no-cache build-base bash coreutils findutils grep curl git sed perl python3 docker sudo \
	&& pip3 install --upgrade pip \
	&& pip3 install docker-compose \
	&& ln -s /usr/bin/python3 /usr/bin/python

ENTRYPOINT ["/bin/bash"]

ARG GIT_COMMIT=unknown
ARG GIT_BRANCH=unknown
LABEL git-commit=$GIT_COMMIT git-branch=$GIT_BRANCH
