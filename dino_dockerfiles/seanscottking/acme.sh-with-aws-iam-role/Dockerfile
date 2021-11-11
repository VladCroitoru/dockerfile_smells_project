FROM neilpang/acme.sh

ENV AWS_ROLE_ARN $AWS_ROLE_ARN
ENV AWS_ROLE_NAME $AWS_ROLE_NAME

RUN apk --no-cache add -f jq python py-pip libidn && rm -rf /var/cache/apk/*
RUN pip install awscli

COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["--help"]
