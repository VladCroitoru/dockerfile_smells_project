# buster-slim is the first version with Tesseract 4.0.
# Alpine would be nice, but it doesn't have good-enough Java
FROM debian:buster-slim AS os

# the mkdir is for https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199#23
RUN set -x \
  && mkdir -p /usr/share/man/man1 \
  && apt-get update && apt-get install -y --no-install-recommends \
    default-jre-headless \
    tesseract-ocr \
    tesseract-ocr-ara \
    tesseract-ocr-cat \
    tesseract-ocr-ces \
    tesseract-ocr-deu \
    tesseract-ocr-eng \
    tesseract-ocr-fra \
    tesseract-ocr-ita \
    tesseract-ocr-nld \
    tesseract-ocr-nor \
    tesseract-ocr-por \
    tesseract-ocr-ron \
    tesseract-ocr-rus \
    tesseract-ocr-spa \
    tesseract-ocr-swe \
    jq \
    ca-certificates \
    openssl \
    tini \
  && rm -rf /var/lib/apt/lists/*

FROM os AS build
RUN set -x \
  && apt-get update && apt-get install -y --no-install-recommends wget unzip \
  && wget -P ~ https://github.com/sbt/sbt/releases/download/v1.1.2/sbt-1.1.2.zip \
  && (cd ~ && unzip sbt-1.1.2.zip) \
  && rm -f ~/sbt-1.1.2.zip
COPY java/ /app/java/
RUN cd /app/java/ && java -jar ~/sbt/bin/sbt-launch.jar assembly


FROM overview/overview-convert-framework:0.0.16 AS framework
# multi-stage build


FROM os AS base
WORKDIR /app
COPY --from=framework /app/run /app/run
COPY --from=framework /app/convert-single-file /app/convert
COPY --from=build /app/java/target/scala-2.12/convert-pdfocr.jar /app/
COPY ./do-convert-single-file /app/do-convert-single-file
CMD [ "/usr/bin/tini", "/app/run" ]


FROM base AS test
COPY --from=framework /app/test-convert-single-file /app/
COPY test/ /app/test/
RUN [ "/app/test-convert-single-file" ]
CMD [ "true" ]


FROM base AS production
