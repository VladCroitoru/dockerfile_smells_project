FROM openshift/base-centos7

# Inform users who's the maintainer of this builder image
MAINTAINER Jorge Morales <jmorales@redhat.com>

# Inform about software versions being used inside the builder
ENV LIGHTTPD_VERSION=1.4.35

# Set labels used in OpenShift to describe the builder images
LABEL io.k8s.description="Platform for serving static HTML files" \
      io.k8s.display-name="Lighttpd 1.4.35" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,html,lighttpd"

# Install the required software, namely Lighttpd and
RUN yum install -y java-1.8.0-openjdk-devel lighttpd && \
    yum clean all -y

# Add environment to locate jdk
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0

RUN yum install -y centos-release-scl && \
    yum-config-manager --enable centos-sclo-rh-testing && \
    INSTALL_PKGS="rh-ruby23 rh-ruby23-ruby-devel rh-ruby23-rubygem-rake rh-ruby23-rubygem-bundler" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && rpm -V $INSTALL_PKGS && \
    yum clean all -y

# Each language image can have 'contrib' a directory with extra files needed to
# run and build the applications.
COPY ./contrib/ /opt/app-root

# Install ascii_binder rubygem
RUN source scl_source enable rh-ruby23 && \
    gem install listen -v 3.1.0 && \
    gem install ascii_binder 

# We need to set UTF-8 in the container for asciibinder to work
ENV LANG=en_US.UTF-8    

# Although this is defined in openshift/base-centos7 image it's repeated here
# to make it clear why the following COPY operation is happening
LABEL io.openshift.s2i.scripts-url=image:///usr/libexec/sti
# Copy the S2I scripts from ./.sti/bin/ to /usr/libexec/sti
COPY ./.sti/bin/ /usr/libexec/sti

# Copy the lighttpd configuration file
COPY ./etc/ /opt/app-root/etc

# Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:1001 /opt/app-root

# Set the default user for the image, the user itself was created in the base image
USER 1001

# Specify the ports the final image will expose
EXPOSE 8080

# Set the default CMD to print the usage of the image, if somebody does docker run
CMD ["/usr/libexec/sti/usage"]
