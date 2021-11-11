# Custom Dockerfile to add German OCR library
# This Dockerfile uses the official Mayan EDMS image
# as a base.

FROM mayanedms/mayanedms

ENV DEBIAN_FRONTEND noninteractive

# Install Ubuntu German OCR package and clean up afterwards

RUN apt-get update && \
apt-get install -y --no-install-recommends \
tesseract-ocr-deu && \
apt-get clean autoclean && \
apt-get autoremove -y && \
rm -rf /var/lib/apt/lists/* && \
rm -f /var/cache/apt/archives/*.deb

# Retain the original entrypoint and command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["mayan:start"]

