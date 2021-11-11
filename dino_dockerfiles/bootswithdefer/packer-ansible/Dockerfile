FROM hashicorp/packer:light
MAINTAINER Jesse DeFer <packer-ansible@dotd.com>

ENV DOCKER_CHANNEL stable
ENV DOCKER_VERSION 20.10.8

RUN adduser -D -u 1000 jenkins

RUN mkdir -p /home/jenkins/.ssh && chmod 0700 /home/jenkins/.ssh && echo "github.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==" > /home/jenkins/.ssh/authorized_keys > /home/jenkins/.ssh/known_hosts && chmod 0600 /home/jenkins/.ssh/* && chown -R jenkins:jenkins /home/jenkins/.ssh

RUN apk --no-cache add git openssh-client rsync jq py-pip py-boto py-six py-cryptography py-bcrypt py-asn1crypto py-jsonschema py-pynacl py-asn1 py-markupsafe py-paramiko py-dateutil py-docutils py-rsa libxml2 libxslt libffi-dev openssl-dev make gcc python3-dev musl-dev linux-headers libxml2-dev libxslt-dev postgresql-dev zip && \
    pip install ansible jsonmerge awscli boto boto3 hvac ansible-modules-hashivault molecule python-gilt python-jenkins lxml openshift docker docker-compose mitogen yamale ansible-lint yamllint kubernetes-validate psycopg2 dnspython && \
    apk del gcc python3-dev musl-dev linux-headers libxml2-dev libxslt-dev libffi-dev openssl-dev make

RUN set -eux; \
	\
# this "case" statement is generated via "update.sh"
	apkArch="$(apk --print-arch)"; \
	case "$apkArch" in \
		x86_64) dockerArch='x86_64' ;; \
		armhf) dockerArch='armel' ;; \
		aarch64) dockerArch='aarch64' ;; \
		ppc64le) dockerArch='ppc64le' ;; \
		s390x) dockerArch='s390x' ;; \
		*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\
	esac; \
	\
	if ! wget -nv -O docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz"; then \
		echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from '${DOCKER_CHANNEL}' for '${dockerArch}'"; \
		exit 1; \
	fi; \
	\
	tar --extract \
		--file docker.tgz \
		--strip-components 1 \
		--directory /usr/local/bin/ \
	; \
	rm docker.tgz; \
	\
	dockerd --version; \
        docker --version

RUN ln -s /usr/bin/python3 /usr/bin/python

COPY plugins /usr/share/ansible/plugins/

RUN ansible-galaxy collection install infoblox.nios_modules -p /usr/share/ansible/collections

ENV ANSIBLE_FORCE_COLOR=True
ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_PIPELINING=True
ENV ANSIBLE_FORKS=25
ENV AWS_DEFAULT_REGION=us-west-2

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
