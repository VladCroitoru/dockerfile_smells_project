FROM alpine:3.6
RUN apk add --no-cache \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        && \
    pip install --upgrade awscli s3cmd python-magic && \
    apk --purge del py-pip
