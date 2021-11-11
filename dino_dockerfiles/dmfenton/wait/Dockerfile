FROM alpine:3.4

RUN apk update && apk add bash curl coreutils

RUN curl -s -o /usr/bin/wait_for_it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh

RUN chmod +x /usr/bin/wait_for_it.sh

ENTRYPOINT ["/usr/bin/wait_for_it.sh"]

CMD ["--help"]
