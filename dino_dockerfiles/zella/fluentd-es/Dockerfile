# fluentd/Dockerfile
FROM fluent/fluentd:v0.12-debian

COPY conf/fluent.conf /fluentd/etc/fluent.conf

RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri", "--version", "1.9.2"]