FROM registry.fedoraproject.org/fedora:latest

LABEL maintainer="Ralph Bean" \
      summary="A prometheus exporter for koji." \
      distribution-scope="public"

RUN dnf install -y --setopt=tsflags=nodocs \
                python3-pip \
                python3-devel \
                krb5-devel \
                gcc \
    && dnf clean all

COPY requirements.txt /usr/local/requirements.txt
RUN pip3 install --no-dependencies -r /usr/local/requirements.txt

# Allow a non-root user to install a custom root CA at run-time
RUN chmod g+w /etc/pki/tls/certs/ca-bundle.crt

COPY koji-prometheus-exporter.py /usr/local/bin/.
COPY docker/ /docker/

USER 1001
EXPOSE 8000
ENTRYPOINT ["/docker/entrypoint.sh", "/usr/local/bin/koji-prometheus-exporter.py"]
