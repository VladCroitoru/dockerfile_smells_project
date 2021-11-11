FROM huygensing/timbuctoo-faceted-search-indexer:buildbase

COPY dcar /app/dcar
COPY womenwriters /app/womenwriters
COPY federated-indexer /app/federated-indexer
COPY generic-indexer /app/generic-indexer
COPY lib /app/lib
COPY webserver /app/webserver

CMD ["/app/webserver/run.sh"]
