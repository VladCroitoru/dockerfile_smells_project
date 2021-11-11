FROM alpine:3.5

ENV TF_VERSION "0.9.4"


RUN apk --update add \
      bash \
      curl \
    && curl -Ls https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip > /tmp/tf.zip \
    && unzip /tmp/tf.zip -d /bin/ \
    && rm /tmp/* /var/cache/apk/*

ADD entrypoint.sh /bin/entrypoint.sh

VOLUME /app
WORKDIR /app

ENTRYPOINT ["entrypoint.sh"]
