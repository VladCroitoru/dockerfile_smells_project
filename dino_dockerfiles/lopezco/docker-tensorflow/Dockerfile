FROM gcr.io/tensorflow/tensorflow:latest-py3

# Pillow needs libjpeg by default as of 3.0.
RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libjpeg8-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install scikit-learn Pillow
WORKDIR /notebooks

COPY entrypoint.sh /
RUN chmod +x /*.sh

ENTRYPOINT ["/entrypoint.sh"]

