FROM ubuntu:trusty
MAINTAINER Hans-Harro Horn <h.h.horn@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
	apt-get install -y \
		software-properties-common \
		texlive-latex-base \
		dvipng \
		libssl-dev \
		gnutls-bin \
		libav-tools # ffmpeg

RUN apt-add-repository -y ppa:aims/sagemath && \
	apt-get update && \
	apt-get install -y \
		sagemath-upstream-binary

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sage -i pyopenssl

RUN useradd -m sage

USER sage

EXPOSE 8080

ENTRYPOINT ["/usr/bin/sage", "-c"]

CMD ["notebook(interface='', automatic_login=False, secure=True, accounts=True, ulimit='-v 500000')"]

