FROM fedora:32
LABEL \
    name="Operators Manifests Push Service" \
    vendor="Red Hat, Inc" \
    maintainer="Martin Basti <mbasti@redhat.com>" \
    license="GPLv3"

# The caller can optionally provide a cacert url
ARG cacert_url=undefined

ENV WORKERS_NUM 8
# Explicit worker timeout is 30 seconds.
ENV WORKER_TIMEOUT 30

WORKDIR /src
RUN dnf -y install \
    python3-flask \
    python3-gunicorn \
    python3-jsonschema \
    python3-koji \
    python3-pip \
    python3-pyyaml \
    python3-requests \
    python3-ruamel-yaml \
    python3-semver \
    python3-validators \
    && dnf -y clean all \
    && rm -rf /tmp/*

RUN if [ "$cacert_url" != "undefined" ]; then \
        cd /etc/pki/ca-trust/source/anchors \
        && curl -O $cacert_url \
        && update-ca-trust extract; \
    fi
# This will allow a non-root user to install a custom root CA at run-time
RUN chmod 777 /etc/pki/tls/certs/ca-bundle.crt
COPY . .
RUN pip3 install --require-hashes --no-deps -r requirements-operator-courier.txt
RUN pip3 install . --no-deps
USER 1001
EXPOSE 8080
ENTRYPOINT docker/install-ca.sh && gunicorn-3 --workers ${WORKERS_NUM} --timeout ${WORKER_TIMEOUT} --bind 0.0.0.0:8080 --access-logfile=- --enable-stdio-inheritance omps.app:app
