ARG branch=latest
FROM cccs/assemblyline-v4-service-base:$branch AS base

ENV SERVICE_PATH suricata_.suricata_.Suricata
ENV SURICATA_VERSION 6.0.3

USER root

RUN echo 'deb http://deb.debian.org/debian stretch-backports main' >> /etc/apt/sources.list

# Install APT dependancies
RUN apt-get update && apt-get install -y wget curl \
  libpcre3 libpcre3-dbg libpcre3-dev build-essential libpcap-dev   \
  libnet1-dev libyaml-0-2 libyaml-dev pkg-config zlib1g zlib1g-dev \
  libcap-ng-dev libcap-ng0 make libmagic-dev libjansson-dev\
  libnss3-dev libgeoip-dev liblua5.1-dev libhiredis-dev libevent-dev \
  python-yaml rustc cargo autoconf \
  && rm -rf /var/lib/apt/lists/*

FROM base AS build

# Install PIP dependancies
USER assemblyline
RUN touch /tmp/before-pip
RUN pip install --no-cache-dir --user \
  simplejson \
  python-dateutil \
  suricata-update \
  retrying && rm -rf ~/.cache/pip

USER root
RUN ln -s /var/lib/assemblyline/.local /root/.local

# Install rustup (purge rustc)
RUN apt remove --purge -y rustc
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
SHELL ["bash", "-lc"]
RUN source $HOME/.cargo/env

# Build suricata
RUN wget -O /tmp/suricata-${SURICATA_VERSION}.tar.gz https://www.openinfosecfoundation.org/download/suricata-${SURICATA_VERSION}.tar.gz
RUN tar -xvzf /tmp/suricata-${SURICATA_VERSION}.tar.gz -C /tmp
WORKDIR /tmp/suricata-${SURICATA_VERSION}
RUN ./configure --disable-gccmarch-native --prefix=/build/ --sysconfdir=/etc/ --localstatedir=/var/ \
  --enable-python --enable-rust --enable-lua
RUN make -C /tmp/suricata-${SURICATA_VERSION}
RUN make -C /tmp/suricata-${SURICATA_VERSION} install
RUN make -C /tmp/suricata-${SURICATA_VERSION} install-full
RUN ldconfig /usr/local/lib

# Install suricata pip package
ENV PATH="/build/bin:$PATH"
ENV TMPDIR=/tmp/suricata-${SURICATA_VERSION}
RUN pip install --no-cache-dir --user /tmp/suricata-${SURICATA_VERSION}/python

# Install stripe
COPY suricata_/stripe/* /tmp/stripe/
RUN /usr/bin/gcc -o /build/bin/stripe /tmp/stripe/stripe.c

# Remove files that existed before the pip install so that our copy command below doesn't take a snapshot of
# files that already exist in the base image
RUN find /var/lib/assemblyline/.local -type f ! -newer /tmp/before-pip -delete

# Switch back to root and change the ownership of the files to be copied due to bitbucket pipeline uid nonsense
RUN chown root:root -R /var/lib/assemblyline/.local

FROM base

# Get the updated local dir from builder
COPY --chown=assemblyline:assemblyline --from=build /var/lib/assemblyline/.local /var/lib/assemblyline/.local
COPY --from=build /build/ /usr/local/
COPY --from=build /etc/suricata/ /etc/suricata/
COPY --from=build /var/log/suricata/ /var/log/suricata/
COPY --from=build /usr/lib /usr/lib

ENV LD_LIBRARY_PATH=/usr/local/lib
# Create all suricata directories and set permissions
RUN mkdir -p /mount/updates && chown -R assemblyline /mount/updates
RUN mkdir -p /etc/suricata && chown -R assemblyline /etc/suricata
RUN mkdir -p /var/lib/suricata && chown -R assemblyline /var/lib/suricata
RUN mkdir -p /var/log/suricata && chown -R assemblyline /var/log/suricata
RUN mkdir -p /var/run/suricata && chown -R assemblyline /var/run/suricata

# Update suricata config
COPY suricata_/conf/suricata.yaml /etc/suricata/
RUN chown assemblyline /etc/suricata/suricata.yaml
RUN sed -i -e 's/__HOME_NET__/any/g' /etc/suricata/suricata.yaml
RUN sed -i -e 's/__RULE_FILES__/rule-files: []/g' /etc/suricata/suricata.yaml

# Update local rules using suricata-update script here
RUN touch /etc/suricata/suricata-rules-update
RUN chown -R assemblyline /var/lib/suricata/
RUN chown assemblyline /etc/suricata/suricata-rules-update

# Switch to assemblyline user
USER assemblyline

# Copy Suricata service code
WORKDIR /opt/al_service
COPY . .

# Patch version in manifest
ARG version=4.0.0.dev1
USER root
RUN sed -i -e "s/\$SERVICE_TAG/$version/g" service_manifest.yml

# Switch to assemblyline user
USER assemblyline
