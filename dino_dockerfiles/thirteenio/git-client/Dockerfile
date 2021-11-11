FROM alpine AS compile-image

LABEL maintainer Christophe Deliens <chris@deliens.be>

WORKDIR /tmp
RUN apk --update add build-base openssh curl autoconf zlib-dev curl-dev

# TODO: optimise compiled binary size
ENV GIT_VERSION 2.15.0
RUN mkdir -p /usr/src/git && \
	curl -L https://github.com/git/git/archive/v$GIT_VERSION.tar.gz | tar xvz -C /usr/src/git --strip 1 && \
	cd /usr/src/git && \
	make configure && \
	./configure NO_TCLTK=YesPlease NO_PERL=YesPlease NO_EXPAT=YesPlease NO_GETTEXT=YesPlease && \
	make install

# ---

FROM alpine AS final-image

RUN apk --update add openssh && \
	rm -rf /var/lib/apt/lists/* && \
	rm /var/cache/apk/*
	
COPY --from=compile-image /usr/local/bin/git* /usr/local/bin/

VOLUME /git
WORKDIR /git

ENTRYPOINT ["git"]
CMD ["--help"]