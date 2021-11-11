FROM python:3.6
MAINTAINER Ederson Torresini <boidacarapreta@gmail.com>

ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="kididcca: assinante MQTT" \
      org.label-schema.description="Kit Introdutório de Internet das Coisas com Arduino" \
      org.label-schema.license="MIT" \
      org.label-schema.url="https://projetos.sj.ifsc.edu.br" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/kididcca/mqtt-mongo" \
      org.label-schema.vendor="IFSC" \
      org.label-schema.version="0.3" \
      org.label-schema.schema-version="1.0"

COPY docker-entrypoint.sh requirements.txt /
RUN chmod 0755 /docker-entrypoint.sh && \
    pip install -r /requirements.txt && \
    groupadd assinante && \
    useradd -g assinante -d /assinante -s /bin/false assinante && \
    mkdir -p /assinante/html && \
    chown -R assinante:assinante /assinante && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY assinante.py /assinante/

WORKDIR "/assinante"
USER "assinante"
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/local/bin/python", "assinante.py"]
