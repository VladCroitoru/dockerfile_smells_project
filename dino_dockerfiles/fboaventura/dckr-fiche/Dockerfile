FROM joeshaw/busybox-nonroot

ENV DOMAIN "localhost"
ENV SLUG 8
ENV BUFFER 4096
ENV PORT "9999"

ADD files/fiche-static /fiche
ADD files/index.html /data/
RUN chown -R nobody /data

EXPOSE 9999

VOLUME /data

USER nobody

CMD /fiche -d ${DOMAIN} -o /data -l /dev/stdout -p ${PORT} -s ${SLUG} -B ${BUFFER}

# Metadata params
ARG BUILD_DATE
ARG VERSION
ARG VCS_URL
ARG VCS_REF
ARG AUTHOR
ARG VENDOR

# Metadata
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Soluspipe/Fiche" \
      org.label-schema.description="This is the same software that runs termbin.com" \
      org.label-schema.url="https://termpaste.cf" \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vendor=$VENDOR \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0" \
      org.label-schema.author="$AUTHOR" \
      com.em13.docker.dockerfile="/Dockerfile" \
      com.em13.license="MIT"

