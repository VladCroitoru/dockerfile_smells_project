FROM alpine AS builder

RUN apk add --update \
		make \
		g++ \
		cmake \
		zlib-dev \
		openssl-dev \
		protobuf-dev \
		xz-dev \
		lzo-dev \
		;

ADD . /usr/src/
WORKDIR /usr/src/

RUN cmake .
RUN make

FROM alpine:3.7
LABEL maintainer="Matthew Endsley <mendsley@gmail.com>"

RUN apk add --update openssl zlib protobuf xz lzo
COPY --from=builder /usr/src/zbackup /usr/bin/zbackup

ENTRYPOINT ["/usr/bin/zbackup"]
CMD ["--help"]
