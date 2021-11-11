FROM python:3.6

MAINTAINER yohanyflores@gmail.com

ENV DEBIAN_FRONTEND noninteractive

ENV TZ America/Caracas

# Especifica el sufijo  para los indices.
ENV INDEX_NAME_SUFFIX "index"

# Especifica el template a cargar, por defecto se genera el template de aurora.
ENV CONFIG_TEMPLATE "aurora"

# instalamos mongo connector.
RUN apt-get update && apt-get install -y build-essential python-dev \
    && pip install mongo-connector[elastic5]==2.5.1 \
    && pip install elastic2-doc-manager[elastic5]==0.3.0

# creamos la carpeta para las configuraciones
RUN mkdir -p /conf.d

# añadimos las plantillas
ADD conf-templates /conf-templates

# Creamos el entry-point
ADD imolko-entrypoint.sh /imolko-entrypoint.sh

ENTRYPOINT ["/imolko-entrypoint.sh"]

CMD ["mongo-connector", "-c", "/conf.d/aurora.json"]

VOLUME /data
