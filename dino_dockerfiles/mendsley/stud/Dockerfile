FROM alpine:3.12.0 AS builder

RUN apk add --update \
		bsd-compat-headers \
		gcc \
		libev-dev \
		make \
		musl-dev \
		openssl-dev \
		zlib-dev \
		;

ADD . /usr/src/stud/
RUN make -C /usr/src/stud/

FROM alpine:3.12.0
LABEL maintainer="Matthew Endsley <mendsley@gmail.com>"

RUN apk add --update \
		openssl=1.1.1g-r0 \
		libev=4.33-r0 \
		zlib=1.2.11-r3 \
	&& rm -rf /var/cache/apk/* \
	&& mkdir -p /cert /sock \
	;

COPY --from=builder /usr/src/stud/stud /usr/bin/stud
COPY --from=builder /usr/src/stud/example.com.pem /etc/keycert.pem

EXPOSE 443

ENTRYPOINT ["/usr/bin/stud"]
