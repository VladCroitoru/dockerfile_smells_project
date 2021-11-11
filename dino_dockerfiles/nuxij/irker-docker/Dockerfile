FROM alpine

LABEL maintainer "Joe Eaves <joe.eaves@shadowacre.ltd>"

ENV BUILD_PACKAGES "make asciidoc python-dev xmlto"

RUN apk add --update git python $BUILD_PACKAGES  &&\
	git clone https://gitlab.com/esr/irker.git && \
	cd irker && \
	make && make install && \
	apk del $BUILD_PACKAGES

ENTRYPOINT ["/usr/bin/irkerd"]
