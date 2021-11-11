FROM alpine:edge
MAINTAINER mikejoh
RUN apk add --no-cache \
    ca-certificates \
    python \
    ansible \
    && addgroup -S ansible && adduser -S -g ansible ansible
USER ansible:ansible
WORKDIR /ansible
ENTRYPOINT ["ansible-playbook"]
