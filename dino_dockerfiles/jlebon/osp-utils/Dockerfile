FROM fedora:24
MAINTAINER Jonathan Lebon <jlebon@redhat.com>

RUN dnf install -y \
		gcc \
		python3-devel \
		redhat-rpm-config && \
	dnf clean all

# We use --net=host here to reduce potential issues with
# reaching the OpenStack instance.

# NB: we disable -t here because it would fail on Jenkins.
# If you're running this locally, you can get the progress
# bar by doing e.g. atomic run --opt1='-ti'.

LABEL RUN="/usr/bin/docker run --rm \
             --net=host \
             --privileged \
             -v \"\$PWD:\$PWD\" \
             --workdir \"\$PWD\" \
             -e OS_AUTH_URL \
             -e OS_TENANT_ID \
             -e OS_USERNAME \
             -e OS_PASSWORD \
             \${OPT1} \
             \${IMAGE}"

ENV PYTHONUNBUFFERED 1

COPY . /osp-utils

RUN pip3 install -r /osp-utils/requirements.txt

ENTRYPOINT ["/osp-utils/main.py"]
