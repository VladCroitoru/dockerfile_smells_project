#
# Copyright Red Hat, Inc.
#
# SPDX-License-Identifier: GPL-2.0-or-later
#

ARG OS_VERSION="latest"
ARG COPR_REPO="@pki/master"

################################################################################
FROM registry.fedoraproject.org/fedora:$OS_VERSION AS ldapjdk-builder

ARG COPR_REPO
ARG BUILD_OPTS

# Enable COPR repo if specified
RUN if [ -n "$COPR_REPO" ]; then dnf install -y dnf-plugins-core; dnf copr enable -y $COPR_REPO; fi

# Import LDAPJDK sources
COPY . /tmp/ldapjdk/
WORKDIR /tmp/ldapjdk

# Build LDAPJDK packages
RUN dnf install -y git rpm-build
RUN dnf builddep -y --spec ldapjdk.spec
RUN ./build.sh $BUILD_OPTS --work-dir=build rpm

RUN ls -la && ls -la build

################################################################################
FROM registry.fedoraproject.org/fedora:$OS_VERSION AS ldapjdk-runner

ARG COPR_REPO

EXPOSE 389 8080 8443

# Enable COPR repo if specified
RUN if [ -n "$COPR_REPO" ]; then dnf install -y dnf-plugins-core; dnf copr enable -y $COPR_REPO; fi

# Import LDAPJDK packages
COPY --from=ldapjdk-builder /tmp/ldapjdk/build/RPMS /tmp/RPMS/

# Install LDAPJDK packages
RUN dnf localinstall -y /tmp/RPMS/*; rm -rf /tmp/RPMS

# Install systemd to run the container
RUN dnf install -y systemd

CMD [ "/usr/sbin/init" ]
