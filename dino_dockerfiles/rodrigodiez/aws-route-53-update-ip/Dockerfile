FROM alpine:3.6
RUN apk -v --update add \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        bind-tools \
        bash \
        && \
    pip install --upgrade awscli==1.11.188 s3cmd==2.0.1 python-magic && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*

RUN mkdir -p /opt/local/aws-route-53-update-ip
COPY update.sh /opt/local/aws-route-53-update-ip
RUN chmod +x /opt/local/aws-route-53-update-ip/update.sh

CMD "/opt/local/aws-route-53-update-ip/update.sh"
