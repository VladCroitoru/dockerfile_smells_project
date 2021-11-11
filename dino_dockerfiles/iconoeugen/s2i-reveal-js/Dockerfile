FROM openshift/base-centos7
MAINTAINER Horatiu Vlad <horatiu@vlad.eu>

EXPOSE 8080

ENV REVEAL_JS_VERSION=3.4.1 \
    PATH=${HOME}/.local/bin/:$PATH

LABEL io.k8s.description="Platform for building and running Reveal.JS presentations" \
      io.k8s.display-name="Node.JS" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,javascript,nodejs"

RUN yum install -y epel-release && \
    INSTALL_PKGS="nodejs npm nss_wrapper" && \
    yum install -y --setopt=tsflags=nodocs --enablerepo=centosplus ${INSTALL_PKGS} && \
    rpm -V ${INSTALL_PKGS} && \
    yum clean all -y

RUN curl https://codeload.github.com/hakimel/reveal.js/tar.gz/${REVEAL_JS_VERSION} | tar -C /opt/app-root -xz && \
    fix-permissions /opt/app-root/reveal.js-${REVEAL_JS_VERSION} && \
    ln -s /opt/app-root/reveal.js-${REVEAL_JS_VERSION} /opt/app-root/reveal.js && \
    cd /opt/app-root/reveal.js && \
    npm install

# Copy the S2I scripts from the specific language image to ${STI_SCRIPTS_PATH}.
COPY ./.s2i/bin/ ${STI_SCRIPTS_PATH}

# Each language image can have 'contrib' a directory with extra files needed to
# run and build the applications.
COPY ./contrib/ /opt/app-root

# In order to drop the root user, we have to make some directories world
# writable as OpenShift default security model is to run the container under
# random UID.
RUN chown -R 1001:0 /opt/app-root && chmod -R og+rwX /opt/app-root

USER 1001

# Set the default CMD to print the usage of the language image.
CMD ${STI_SCRIPTS_PATH}/usage
