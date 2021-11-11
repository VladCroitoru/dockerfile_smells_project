FROM golang:1.13-alpine
RUN apk add --update --no-cache nodejs yarn hugo groff less python py-pip git make zip && \
    pip install awscli && \
    apk --purge -v del py-pip