FROM grafana/grafana:8.1.3

USER root
ENV VERSION=1.0.2
RUN wget https://github.com/org-insights/aws-s-3/releases/download/v${VERSION}/itay-s3-datasource-${VERSION}.zip \
 -O /var/lib/grafana/plugins/itay-s3-datasource-${VERSION}.zip \
 && cd /var/lib/grafana/plugins \
 && unzip itay-s3-datasource-${VERSION}.zip \
 && rm itay-s3-datasource-${VERSION}.zip

# ADD dist /var/lib/grafana/plugins/aws-s-3/dist
# ENV GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS orginsights-s3-datasource
# ENV GF_SERVER_HTTP_PORT 80

USER grafana