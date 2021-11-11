FROM alpine

RUN apk --update add curl && \
    curl -Lo /tmp/terraform.zip https://releases.hashicorp.com/terraform/0.10.0-rc1/terraform_0.10.0-rc1_linux_amd64.zip && \
    unzip /tmp/terraform.zip -d /usr/local/bin/

ADD plan /plan
ADD entrypoint.sh /
WORKDIR /output

ENTRYPOINT ["/entrypoint.sh"]
