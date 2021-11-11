FROM arangodb/arangodb:3.2.4
LABEL maintainer="pctao.tw@gmail.com"

RUN apt-get update \
 && apt-get install -y procps jq python3 python3-requests python3-boto python3-boto3 openssl groff-base unzip

ADD https://s3.amazonaws.com/aws-cli/awscli-bundle.zip /tmp/awscli-bundle.zip

RUN unzip -d /tmp/ /tmp/awscli-bundle.zip \
 && python3 /tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \
 && rm -f /tmp/awscli-bundle.zip \
 && rm -rf /tmp/awscli-bundle

COPY ecs-get-port-mapping.py /usr/local/bin/ecs-get-port-mapping.py
COPY get_all_8529.sh /usr/local/bin/get_all_8529.sh
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
