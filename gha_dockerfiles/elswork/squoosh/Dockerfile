ARG BASEIMAGE=node:12.18.3-alpine
FROM ${BASEIMAGE}

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL mantainer="Eloy Lopez <elswork@gmail.com>" \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="squoosh" \
    org.label-schema.description="squoosh is a general purpose tool" \
    org.label-schema.url="https://deft.work/squoosh" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url="https://github.com/elswork/squoosh" \
    org.label-schema.vendor="Deft Work" \
    org.label-schema.version=$VERSION \
    org.label-schema.schema-version="1.0"

# RUN apk add --no-cache squoosh
RUN npm i -g @squoosh/cli
WORKDIR /data