# buster-slim is the first version with Tesseract 4.0.
# Alpine would be nice, but we already use buster-slim in pdfocr and
# we want the exact same data files that a user might be expected to
# use at home
FROM debian:buster-slim AS os
RUN set -x \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    file \
    imagemagick \
    jq \
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
    tesseract-ocr-rus \
    tesseract-ocr-spa \
    tesseract-ocr-swe \
    python3-pip \
    python3-setuptools \
  && pip3 install img2pdf \
  && apt-get clean -y \
  && rm -rf /var/cache/debconf/* /var/lib/apt/lists/* /var/log/* /tmp/* /var/tmp/*

FROM overview/overview-convert-framework:0.0.17 AS framework
# multi-stage build

FROM os AS base
WORKDIR /app
COPY --from=framework /app/run /app/run
COPY --from=framework /app/convert-single-file /app/convert
COPY ./do-convert-single-file /app/do-convert-single-file
CMD [ "/app/run" ]

FROM base AS test
COPY --from=framework /app/test-convert-single-file /app/
COPY test/ /app/test/
RUN [ "/app/test-convert-single-file" ]
CMD [ "true" ]

FROM base AS production
