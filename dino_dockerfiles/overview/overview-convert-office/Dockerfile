# multi-stage build
FROM alpine:3.11.6 AS os
RUN set -x \
  && apk add --update --no-cache \
    libreoffice \
    qpdf-libs \
    ttf-freefont \
    msttcorefonts-installer \
    tini \
  && update-ms-fonts \
  && fc-cache -f

# Generate clean profile directory. soffice.bin should exit with code 81
# on first run, when it's creating the profile directory.
#
# Generate the profile in its final location, in case there are any
# absolute paths. ([2020-05-08, adamhooper] I have no idea what's in a
# profile dir.)
ENV PROFILE_DIR /tmp/soffice-profile
ENV PROFILE_TEMPLATE_DIR /app/soffice-profile-template
RUN mkdir -p /tmp /app \
      && sh -c '/usr/lib/libreoffice/program/soffice.bin --headless --norestore --nolockcheck -env:UserInstallation=file://$PROFILE_DIR; test $? -eq 81' \
      && mv $PROFILE_DIR $PROFILE_TEMPLATE_DIR

WORKDIR /app

FROM os AS build
RUN set -x \
  && apk add --update --no-cache \
    libreofficekit \
    libreoffice-sdk \
    qpdf-dev \
    g++ \
    make

COPY main/ /app/main/
RUN sh -c "cd /app/main && make -j$(nproc)"


FROM overview/overview-convert-framework:0.1.1 AS framework

FROM os AS base
WORKDIR /app
COPY --from=framework /app/run /app/run
COPY --from=framework /app/convert-single-file /app/convert
ENV OFFICE_PATH=/usr/lib/libreoffice
ENV LD_LIBRARY_PATH=/usr/lib/libreoffice/program
COPY ./do-convert-single-file /app/do-convert-single-file
COPY --from=build /app/main/convert-to-pdf-with-metadata /app/convert-to-pdf-with-metadata
CMD [ "tini", "--", "/app/run" ]


FROM base AS test
RUN apk --no-cache add qpdf
COPY --from=framework /app/test-convert-single-file /app/
COPY test/ /app/test/
ENV TIMEOUT 5
RUN [ "/app/test-convert-single-file" ]
CMD [ "true" ]


FROM base AS production
