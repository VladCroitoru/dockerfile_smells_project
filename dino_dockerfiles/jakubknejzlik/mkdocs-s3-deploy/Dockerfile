FROM anigeo/awscli

ENV BUCKET_NAME unknown

RUN apk add --update python3 py-pip && pip3 install mkdocs && rm -rf /var/cache/apk/*

WORKDIR /docs

VOLUME /docs

COPY ./bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh

ENTRYPOINT []
