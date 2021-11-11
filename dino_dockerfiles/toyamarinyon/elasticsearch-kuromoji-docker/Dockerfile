# Install analysis-kuromoji plugin into Official elasticsearch docker image.
FROM docker.elastic.co/elasticsearch/elasticsearch:5.4.1
LABEL maintainer "toyamarinyon <toyamarinyon@gmail.com>"

ENV PLUGIN_LIST='analysis-kuromoji'
RUN for plugin in $PLUGIN_LIST; do elasticsearch-plugin install --batch "$plugin"; done
