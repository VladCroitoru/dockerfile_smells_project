FROM rayproject/ray:latest

USER ray

# WARNING: do not distribute the container since it has secrets on the file system
ARG gcp_creds
ENV CREDS_DIR=/home/ray/creds
ENV GOOGLE_APPLICATION_CREDENTIALS=$CREDS_DIR/gcp-creds.json
RUN mkdir -p $CREDS_DIR
RUN echo "$gcp_creds" > $CREDS_DIR/gcp-creds-base64.json
RUN base64 -d $CREDS_DIR/gcp-creds-base64.json > $GOOGLE_APPLICATION_CREDENTIALS

RUN sudo apt-get update && \
    sudo apt-get install -y \
    emacs-nox \
    htop

ADD . modep-common
RUN pip install --no-cache-dir -r modep-common/requirements.txt
RUN pip install --no-cache-dir modep-common/
