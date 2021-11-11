FROM alpine:3.6
RUN apk -v --no-cache add \
        git \
        less \
        openssh-client \
        py-pip \
        python \
        && \
    pip install --upgrade awsebcli
VOLUME /root/.aws
VOLUME /project
WORKDIR /project
ENTRYPOINT ["eb"]
