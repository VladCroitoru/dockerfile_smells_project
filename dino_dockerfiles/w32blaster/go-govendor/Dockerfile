FROM golang:alpine


RUN apk add --update --no-cache git libressl-dev make && \
    apk del openssl && \

    # install govendor
    go get -u -v github.com/kardianos/govendor && \
    rm -rf /var/cache/apk/* && \
    
    # add few useful aliases to print colored messages to stdout in non-interactive mode
    echo -e '#!/bin/sh\n printf "\033[1;32m$* \033[0m"' > /usr/bin/printGreen && \
    chmod +x /usr/bin/printGreen && \

    echo -e '#!/bin/sh\n printf "\033[1;32m$* \033[0m \n"' > /usr/bin/printGreenln && \
    chmod +x /usr/bin/printGreenln


