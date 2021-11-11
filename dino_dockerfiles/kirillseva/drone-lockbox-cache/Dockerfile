FROM alpine:3.6

MAINTAINER Kirill Sevastyanenko <github.com/kirillseva>

RUN wget "s3.amazonaws.com/aws-cli/awscli-bundle.zip" -O "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    apk add --update groff less python && \
    rm /var/cache/apk/* && \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    rm awscli-bundle.zip && \
    rm -rf awscli-bundle

ADD script.sh /bin/
ADD restore.sh /bin/
ADD update.sh /bin/
RUN chmod +x /bin/script.sh
RUN chmod +x /bin/restore.sh
RUN chmod +x /bin/update.sh
ENTRYPOINT /bin/script.sh
