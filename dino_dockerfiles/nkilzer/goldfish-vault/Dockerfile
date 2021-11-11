FROM golang:alpine

WORKDIR /app
ENV GOLDFISH_VERSION=v0.7.4
COPY config.hcl config.hcl
RUN apk add --update curl && \
    curl -L -o goldfish https://github.com/Caiyeon/goldfish/releases/download/$GOLDFISH_VERSION/goldfish-linux-amd64 && \
    chmod a+x goldfish
    
ENTRYPOINT ["./goldfish", "-config", "config.hcl"]
