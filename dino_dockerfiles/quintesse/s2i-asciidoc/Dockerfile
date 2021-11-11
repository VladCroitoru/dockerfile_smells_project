FROM centos/s2i-base-centos7

# This image provides a Ruby environment with Asciidoctor
# meant to turn Asciidoc files into HTML and server them
# up for public consumption
# (Heavily based on sclorg/s2i-ruby-container)

EXPOSE 8080

ENV RUBY_VERSION 2.4

ENV SUMMARY="Builder image for serving up Asciidoc files" \
    DESCRIPTION="S2I builder image that takes Asciidoc files from a source \
repository, converts them into HTML using Asciidoctor and serves them up \
using a simple HTTP server."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Asciidoc" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,asciidoc" \
      name="quintesse/s2i-asciidoc" \
      maintainer="Tako Schotanus <tschotan@redhat.com>"

# To use subscription inside container yum command has to be run first (before yum-config-manager)
# https://access.redhat.com/solutions/1443553
RUN yum install -y centos-release-scl && \
    INSTALL_PKGS="rh-ruby24 rh-ruby24-ruby-devel rh-ruby24-rubygem-rake rh-ruby24-rubygem-bundler rh-nodejs6 rh-nodejs6-npm " && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && rpm -V $INSTALL_PKGS && \
    yum clean all -y

RUN scl --list
# HACK Crappy way to install Asciidoctor but couldn't get things to work otherwise
RUN LD_LIBRARY_PATH=/opt/rh/rh-ruby24/root/usr/lib64:$LD_LIBRARY_PATH /opt/rh/rh-ruby24/root/usr/bin/gem install -N asciidoctor

# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH
COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# Copy extra files to the image.
COPY ./root/ /

RUN chown -R 1001:0 /opt/app-root && chmod -R ug+rwx /opt/app-root && \
    rpm-file-permissions

USER 1001

# Set the default CMD to print the usage of the language image
CMD $STI_SCRIPTS_PATH/usage
