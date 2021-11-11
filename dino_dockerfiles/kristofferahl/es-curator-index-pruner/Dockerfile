FROM bobrik/curator:5.7.6

USER root:root
RUN apk --no-cache add ca-certificates curl
USER nobody:nobody

COPY entrypoint /
COPY curator.yml /
COPY actions.yml /

ENTRYPOINT ["/entrypoint"]
CMD ["--config", "/curator.yml", "/actions.yml"]
