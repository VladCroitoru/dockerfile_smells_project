FROM trevorj/boilerplate
MAINTAINER Trevor Joynson "<docker@trevor.joynson.io>"

# Latest
ARG SALT_RELEASE="latest"
ARG SALT_PACKAGES="salt-minion salt-master salt-api salt-cloud salt-ssh nacl-tools git"

## Pinned
#ARG SALT_RELEASE="2016.3"

# Lazy automagic (eval'd later, don't judge me)
ARG SALT_APT_RELEASE="\${DISTRIB_RELEASE}/\${DISTRIB_ARCH}/\${SALT_RELEASE}"

# Build repo URL
ARG SALT_APT_REPO="http://repo.saltstack.com/apt/ubuntu/\${SALT_APT_RELEASE}"

# Install salt-minion
COPY build.d $IMAGE_ROOT/build.d
RUN build-parts "$IMAGE_ROOT/build.d"

# Add in files
ADD image $IMAGE_ROOT/

VOLUME ["/etc/salt/pki", "/srv/salt", "/srv/pillar"]
EXPOSE 4505 4506

# Fucking CI docker is from 1999.
#HEALTHCHECK --interval=5m --timeout=3s CMD-SHELL nc -z localhost 4505 && nc -z localhost 4506 || exit 1
