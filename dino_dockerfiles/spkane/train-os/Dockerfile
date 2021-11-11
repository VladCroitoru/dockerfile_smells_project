from fedora:34

RUN useradd -u 500 -m user500 && \
  useradd -u 501 -m user501

RUN dnf install -y \
      hostname \
      iproute \
      iputils \
      tcpdump \
      util-linux \
      ntpsec \
      procps-ng \
      strace \
      bonnie++ \
      stress && \
  dnf clean all

RUN setcap cap_net_raw,cap_net_admin+p /usr/bin/ping && \
  cp /usr/bin/ping /usr/bin/ping-nopriv

