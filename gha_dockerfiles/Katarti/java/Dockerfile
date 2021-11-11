FROM registry.fedoraproject.org/fedora-minimal:34

SHELL ["/bin/bash", "-c"]

ARG JAVA_VERSION=11
RUN microdnf install -y \
  gettext \
  java-${JAVA_VERSION}-openjdk-devel \
  postgresql \
  mariadb \
  tar \
  tzdata \
  netcat \
  wget && \
  microdnf update -y && \
  microdnf clean all

ONBUILD ARG UID=1000
ONBUILD RUN useradd -d /java -l -m -Uu ${UID} -r -s /bin/bash java && \
  chown -R ${UID}:${UID} /java

ONBUILD USER ${UID}:${UID}
ONBUILD ENV JAVA_OPTS="-Djava.net.preferIPv4Stack=true -Xmx1024m -Xms1024m"
