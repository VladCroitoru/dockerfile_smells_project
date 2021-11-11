FROM alpine:latest
RUN apk add --no-cache openssh-client && \
  mkdir -p ~/.ssh && \
  echo -e "Host *\n\tStrictHostKeyChecking no\n\tForwardAgent yes\n\n" > ~/.ssh/config
ADD ./bin/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
