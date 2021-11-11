# # # compute-ca
FROM ocramz/docker-phusion-supervisor

ENV NNODES=2 \
    TLS_DIR=${HOME}/.tls

RUN mkdir -p ${TLS_DIR}


RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates debian-keyring debian-archive-keyring openssl && \
    rm -rf /var/lib/apt/lists/*



# cert creation in bash file
COPY bin/generate-certs.sh ${TLS_DIR}/generate-certs.sh


WORKDIR ${TLS_DIR}

# CMD ${TLS_DIR}/generate-certs.sh ${NNODES}