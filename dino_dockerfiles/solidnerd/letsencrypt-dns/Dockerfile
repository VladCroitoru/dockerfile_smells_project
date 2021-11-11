FROM  quay.io/letsencrypt/letsencrypt:v0.11.1

COPY letsencrypt-hooks/* /letsencrypt/hooks/
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN apt-get update && apt-get install -y curl && \
  chmod +x /letsencrypt/hooks/authenticator.sh \
  /letsencrypt/hooks/cleanup.sh \
  /docker-entrypoint.sh  && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*

ENV PATH="$PATH:/letsencrypt/hooks"

ENTRYPOINT ["/docker-entrypoint.sh"]

VOLUME ["/etc/letsencrypt","/var/lib/letsencrypt","/var/log/letsencrypt"]

ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.license="MIT" \
      org.label-schema.name="letsencrypt-dns" \
      org.label-schema.url="https://github.com/solidnerd/letsencrypt-dns" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/solidnerd/letsencrypt-dns.git" \
      org.label-schema.vcs-type="Git"