FROM alpine

ADD . /empyre

ENV STAGING_KEY=RANDOM

RUN echo "echo Alpine" >> /usr/bin/lsb_release && \
    chmod +x /usr/bin/lsb_release && \
    echo "echo root" >> /usr/bin/logname && \
    chmod +x /usr/bin/logname && \
    apk update && \
    apk add bash && \
    cd /empyre && \
    bash /empyre/setup/install.sh

WORKDIR /empyre

CMD ./empyre
