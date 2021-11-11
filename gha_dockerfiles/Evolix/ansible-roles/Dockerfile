FROM debian:stretch-slim

ENV ROLES_VERSION=${ROLES_VERSION:-unstable}

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
	ansible \
    && rm -rf /var/lib/apt/lists/*

RUN ansible-galaxy install --force \
    --roles-path /etc/ansible \
    "git+https://gitea.evolix.org/evolix/ansible-roles.git,${ROLES_VERSION},roles"

ENV ANSIBLE_FORCE_COLOR=1
ENV ANSIBLE_HOST_KEY_CHECKING=false
ENV ANSIBLE_RETRY_FILES_ENABLED=false
ENV PYTHONUNBUFFERED=1

WORKDIR /data

ENTRYPOINT ["ansible-playbook"]
