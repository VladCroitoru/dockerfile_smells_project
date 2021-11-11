FROM 		gliderlabs/alpine
MAINTAINER 	n0n0x@github

RUN apk add --update bash 

ADD ./start /bin/start

ENV SHELL /bin/bash

ENTRYPOINT ["/bin/start"]
CMD []
