FROM python:3.9-alpine as builder
LABEL maintainer="Ingo Meyer <i.meyer@fz-juelich.de>"

RUN apk --no-cache add build-base cargo libffi-dev openssl-dev rust

WORKDIR /
COPY . gitlab-registry-usage-rest

RUN pip install --no-cache-dir "file:///gitlab-registry-usage-rest"


FROM python:3.9-alpine

RUN apk --no-cache add libffi openssl

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/
COPY --from=builder /usr/local/bin/gitlab-registry-usage-rest /usr/local/bin/gitlab-registry-usage-rest

EXPOSE 80

ENTRYPOINT ["gitlab-registry-usage-rest"]
