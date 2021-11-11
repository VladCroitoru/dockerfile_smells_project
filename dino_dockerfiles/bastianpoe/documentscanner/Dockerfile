FROM debian:stable
MAINTAINER Wolf-Bastian Pöttner <bastian@poettner.de>

# Expose inbox and outbox
VOLUME ["/inbox", "/outbox"]

# Install dependencies
RUN apt-get update && apt-get -y -qq install bash unpaper tesseract-ocr tesseract-ocr-deu imagemagick bc poppler-utils findutils

# Install our scripts
COPY scripts/process.sh scripts/create_pdf.sh /

# Run document processor
CMD ["bash", "/process.sh", "/inbox", "/outbox"]
