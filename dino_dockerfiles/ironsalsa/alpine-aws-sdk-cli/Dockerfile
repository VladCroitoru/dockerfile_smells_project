FROM alpine:3.7
RUN apk -v --update add \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        curl \
        git \
        && \
    pip install --upgrade awscli s3cmd python-magic && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*
CMD ["aws", "--version"]
