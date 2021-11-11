FROM grafana/grafana:latest

ENV UID=1000
ENV GID=1000

COPY ./microbug-run.sh /microbug-run.sh

ENTRYPOINT ["/microbug-run.sh"]
