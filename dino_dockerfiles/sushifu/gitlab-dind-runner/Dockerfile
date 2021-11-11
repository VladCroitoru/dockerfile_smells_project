FROM docker:dind
MAINTAINER SushiFu

RUN apk add --update --no-cache \
		bash \
		ca-certificates \
		git \
		openssl \
		wget \
        openssh

RUN wget -O /usr/bin/gitlab-ci-multi-runner https://gitlab-ci-multi-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-ci-multi-runner-linux-amd64 && \
	chmod +x /usr/bin/gitlab-ci-multi-runner && \
	ln -s /usr/bin/gitlab-ci-multi-runner /usr/bin/gitlab-runner && \
	mkdir -p /etc/gitlab-runner/certs && \
	chmod -R 700 /etc/gitlab-runner

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

VOLUME ["/etc/gitlab-runner"]

ENTRYPOINT ["/entrypoint.sh"]
