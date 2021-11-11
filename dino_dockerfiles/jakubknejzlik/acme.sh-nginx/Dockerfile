FROM nginx:alpine

ADD issue.sh issue.sh

RUN chmod +x /issue.sh && \
  apk update && \
  apk --no-cache add -f openssl curl netcat-openbsd && \
  curl https://get.acme.sh | sh && \
  ln -s /root/.acme.sh/acme.sh /usr/bin/acme.sh
