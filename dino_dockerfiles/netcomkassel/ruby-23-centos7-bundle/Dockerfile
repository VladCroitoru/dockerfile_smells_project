
# ruby-23-centos7-bundle
FROM centos/ruby-23-centos7

# The maintainer name in the image metadata
MAINTAINER Ralf Herzog <ralf.herzog@netcom-kassel.de>

USER root

# Set labels used in OpenShift to describe the builder image
LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="Platform for building ruby 2.3 with some extra dependencies" \
      io.k8s.display-name="Netcom Ruby 2.3" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,ruby,ruby23,rh-ruby23,netcom,firebird,smbclient,smb" \
      name="netcomkassel/ruby-23-centos7-bundle" \
      version="2.3" \
      release="1" \
      maintainer="Ralf Herzog <ralf.herzog@netcom-kassel.de>"

# Install required packages
RUN yum install -y firebird-devel samba-client && yum clean all -y

# Import internal root CA certificate
COPY ./netcom-kassel-CA.crt /etc/pki/ca-trust/source/anchors/netcom-kassel-CA.crt
RUN update-ca-trust

# (optional): Copy the builder files into /opt/app-root
# COPY ./<builder_folder>/ /opt/app-root/

# Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7 image
# sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./s2i/bin/ /usr/libexec/s2i

# Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:1001 /opt/app-root

# This default user is created in the openshift/base-centos7 image
USER 1001

# Set the default port for applications built using this image
EXPOSE 8080

# Set the default CMD for the image
CMD ["/usr/libexec/s2i/usage"]
