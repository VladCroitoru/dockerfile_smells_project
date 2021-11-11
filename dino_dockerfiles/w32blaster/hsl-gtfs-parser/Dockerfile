#
# Stage 1: build
#          download dependencies using govendor and compile the go application
#
FROM w32blaster/go-govendor as builder

RUN mkdir -p /go/src/github.com/w32blaster/hsl-gfts-parser/vendor

ENV GOPATH=/go/
WORKDIR /go/src/github.com/w32blaster/hsl-gfts-parser/


ADD ./*.go /go/src/github.com/w32blaster/hsl-gfts-parser/
ADD ./vendor/vendor.json /go/src/github.com/w32blaster/hsl-gfts-parser/vendor/vendor.json

RUN apk update && apk add --no-cache gcc g++ musl-dev
RUN cd /go/src/github.com/w32blaster/hsl-gfts-parser/ && \
    govendor list && \
    govendor fetch -v +out

RUN CGO_ENABLED=1 GOOS=linux go build -a -installsuffix cgo -o hsl-parser .


#
# Stage 2: runtime container
#
FROM alpine:latest

COPY --from=builder /go/src/github.com/w32blaster/hsl-gfts-parser/hsl-parser /root/
ADD build.sh /root/build.sh

RUN apk update && \

    # install SQlite3 to set up a new database
    # "coreutils" is to use proper version of the "date" function
    apk add --no-cache sqlite wget ca-certificates zip unzip lftp coreutils && \

    # clean up
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/* && \

    mkdir -p /root/db && \

    # make parser runnable
    chmod +x /root/hsl-parser && \
    chmod +x /root/build.sh && \

    # add few useful aliases to print colored messages to stdout in non-interactive mode
    echo -e '#!/bin/sh\n printf "\033[1;32m$* \033[0m \n"' > /usr/bin/printGreenln && \
    chmod +x /usr/bin/printGreenln && \

    # function to get size of a file
    echo -e '#!/bin/sh\n echo `du -h $1 | cut -f1`'  > /usr/bin/getSize && \
    chmod +x /usr/bin/getSize

WORKDIR /root
CMD ["./hsl-parser"]
