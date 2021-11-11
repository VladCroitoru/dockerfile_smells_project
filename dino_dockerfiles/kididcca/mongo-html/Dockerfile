FROM python:3.6
MAINTAINER Ederson Torresini <boidacarapreta@gmail.com>

ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="kididcca: Gerador de páginas HTML" \
      org.label-schema.description="Kit Introdutório de Internet das Coisas com Arduino" \
      org.label-schema.license="MIT" \
      org.label-schema.url="https://projetos.sj.ifsc.edu.br" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/kididcca/mongo-html" \
      org.label-schema.vendor="IFSC" \
      org.label-schema.version="0.1" \
      org.label-schema.schema-version="1.0"

COPY docker-entrypoint.sh requirements.txt /
RUN chmod 0755 /docker-entrypoint.sh && \
    pip install -r /requirements.txt && \
    groupadd cron && \
    useradd -g cron -d /cron -s /bin/false cron && \
    mkdir -p /cron/html && \
    chown -R cron:cron /cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY cron.py /cron/

WORKDIR "/cron"
USER "cron"
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/local/bin/python", "cron.py"]
