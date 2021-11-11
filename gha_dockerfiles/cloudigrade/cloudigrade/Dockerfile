### Base Image
FROM registry.access.redhat.com/ubi8/ubi-minimal:8.4 as base

WORKDIR /opt/cloudigrade

RUN rpm -iv https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm \
    && microdnf update \
    && microdnf install -y \
        git \
        jq \
        libicu \
        nmap-ncat \
        postgresql12-libs \
        procps-ng \
        python39 \
        redhat-rpm-config \
        shadow-utils \
        which \
    && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3.9 /usr/bin/python; fi


### Build virtualenv
FROM base as build

COPY pyproject.toml poetry.lock ./
RUN microdnf install -y \
        gcc \
        libcurl-devel \
        openssl-devel \
        postgresql12-devel \
        python39-devel \
        python39-pip \
    && if [ ! -e /usr/bin/pip ]; then ln -s /usr/bin/pip3.9 /usr/bin/pip ; fi \
    && pip install -U pip \
    && pip install poetry \
    && poetry config virtualenvs.in-project true \
    && PATH="$PATH:/usr/pgsql-12/bin" PYCURL_SSL_LIBRARY=openssl poetry install -n --no-dev


### Create a release image
FROM base as release

ENV VIRTUAL_ENV=/opt/cloudigrade/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Make Ansible happy with arbitrary UID/GID in OpenShift.
RUN chmod g=u /etc/passwd /etc/group

# Grab our built virtualenv
COPY --from=build /opt/cloudigrade/.venv/ .venv/

# Copy in cloudigrade
COPY deployment/playbooks/ ./playbooks
COPY deployment/scripts/cloudigrade_init.sh ./scripts/cloudigrade_init.sh
COPY cloudigrade .

EXPOSE 8000

ENTRYPOINT ["gunicorn"]
CMD ["-c","config/gunicorn.py","config.wsgi"]
