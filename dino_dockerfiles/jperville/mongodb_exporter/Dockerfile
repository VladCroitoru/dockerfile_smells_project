FROM     debian:jessie
EXPOSE     9001

# Add mongodb_exporter binary built after applying https://github.com/percona/mongodb_exporter/pull/38
ADD vendor/mongodb_exporter /bin/mongodb_exporter
RUN chmod +x /bin/mongodb_exporter

ENTRYPOINT [ "/bin/mongodb_exporter" ]
