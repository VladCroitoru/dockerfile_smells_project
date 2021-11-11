#######################
## stage -> builder
#######################
FROM golang:1.8.3-stretch as builder
LABEL maintainer="jmpeso@gmail.com"
ARG RUNTESTS=0
# gcc for cgo
RUN apt-get update && apt-get install -y --no-install-recommends \
		g++ gcc libc6-dev make pkg-config ca-certificates git curl \
	libvips libvips-dev \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# setup go & glide
RUN curl https://glide.sh/get | sh
WORKDIR /go/src/github.com/trilopin/godinary/

# app
ENV SRC_DIR=/go/src/github.com/trilopin/godinary/
COPY . /go/src/github.com/trilopin/godinary/
RUN make get-deps
RUN if [ "$RUNTESTS" = "1" ]; then make test; fi
RUN for i in cmd/*; do go build -o "bin/$(basename $i)" "$i/$(basename $i).go"; done
#######################
## stage -> runner
#######################
FROM debian:stretch as runner
LABEL maintainer="jmpeso@gmail.com"
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*
RUN mkdir /app
COPY --from=builder /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
COPY --from=builder /lib/ /lib/
COPY --from=builder /go/src/github.com/trilopin/godinary/bin/ /app/
ENTRYPOINT ["/app/godinary"]

