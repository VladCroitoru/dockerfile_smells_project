FROM docker:20.10

RUN apk -v --no-cache --update add \
        python3 \
        py-pip \
        groff \
        less \
        mailcap \
        git \
        openssh-client \
        && \
    pip install --upgrade awscli
