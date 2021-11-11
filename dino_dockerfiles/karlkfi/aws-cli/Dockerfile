FROM alpine:3.12
RUN apk -v --no-cache add \
        python3 \
        py3-pip \
        groff \
        less \
        mailcap \
        && \
    pip install --upgrade awscli==1.18.74 s3cmd==2.1.0 python-magic && \
    apk -v --purge del py-pip
VOLUME /root/.aws
VOLUME /project
WORKDIR /project
ENTRYPOINT ["aws"]
