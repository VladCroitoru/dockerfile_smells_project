FROM alpine:latest

RUN \
	mkdir -p /aws && \
	apk -Uuv add bash groff less python py-pip && \
	pip install awscli && \
	apk --purge -v del py-pip && \
	rm /var/cache/apk/*

# Done for convience so we can develop on a Mac with bash from brew
RUN ln -s /bin/bash /usr/local/bin/bash

RUN mkdir /src

COPY src/ /src/

WORKDIR /src

ENTRYPOINT ["./run.sh"]
