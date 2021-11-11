FROM alpine

ENV DEBUG false
ENV AWS_ACCESS_KEY_ID ""
ENV AWS_SECRET_ACCESS_KEY ""
ENV AWS_DEFAULT_REGION ""
ENV AWS_DEFAULT_OUTPUT "json"
ENV AWS_S3_BUCKET ""
ENV AWS_S3_STORAGE_CLASS "STANDARD_IA"

RUN apk add --update docker python py-pip bash && \
    pip install awscli && \
    rm -rf /var/cache/apk/*

ADD entrypoint.sh /
ADD types/ /types/

CMD ["bash", "/entrypoint.sh"]
