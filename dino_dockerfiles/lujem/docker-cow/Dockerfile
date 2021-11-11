FROM alpine

RUN apk add --update curl
RUN curl -L git.io/cow | sh

ENTRYPOINT ["/cow"]
