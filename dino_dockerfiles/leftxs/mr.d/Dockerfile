FROM alpine:latest
MAINTAINER Sven Strack <sven@so36.net>

# Note: This uses the testing repo -> http://pkgs.alpinelinux.org/packages?package=emacs&repo=all&arch=x86_64
RUN apk update && apk add \
	python \
	python-dev \
	build-base \
        ca-certificates \
        aspell-en \
	py-pip \
	enchant \
	--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
	&& rm -rf /var/cache/apk/* \
	&& pip install --upgrade pip \
	&& pip install sphinx \
	pyenchant \
	sphinxcontrib-dashbuilder \
	sphinxcontrib.gist \
	sphinx-rtd-theme \
        sphinxcontrib-spelling


VOLUME ["/build/docs"]

WORKDIR /build

COPY conf conf
COPY spelling_wordlist.txt spelling_wordlist.txt
COPY Makefile /build/Makefile

ENTRYPOINT ["make"]
#CMD ["/bin/ash"]
