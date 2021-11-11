FROM debian:buster-slim

# Install Python, pip, boto3 and python-systemd.
RUN BUILD_DEPS="curl python3-dev python3-pip python3-setuptools pkg-config \
      gcc git libsystemd-dev" \
    VERSION="234"; \
    apt-get update && \
    apt-get install --no-install-recommends --yes python3 $BUILD_DEPS && \
    pip3 install --no-cache-dir boto3 "git+https://github.com/systemd/python-systemd.git/@v$VERSION#egg=systemd" && \
    apt-get purge --auto-remove -y $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*

COPY main.py /main.py
ENTRYPOINT ["python3", "/main.py"]
