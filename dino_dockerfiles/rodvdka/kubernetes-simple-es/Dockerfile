FROM gcr.io/google_containers/elasticsearch:v5.4.0-1

COPY elasticsearch.yml /elasticsearch/config/elasticsearch.yml

COPY run.sh /run.sh

CMD chmod +x /run.sh

ENTRYPOINT ["/bin/sh", "/run.sh"]
