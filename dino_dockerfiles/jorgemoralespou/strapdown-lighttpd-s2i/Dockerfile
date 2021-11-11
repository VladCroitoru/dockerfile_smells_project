FROM openshift/base-centos7

# Inform users who's the maintainer of this builder image
MAINTAINER Jorge Morales <jmorales@redhat.com>

# Inform about software versions being used inside the builder
ENV LIGHTTPD_VERSION=1.4.39

# Set labels used in OpenShift to describe the builder images
LABEL io.k8s.description="Platform for serving static HTML filesi built with strapdown from Markdown" \
      io.k8s.display-name="strapdown-lighttpd-s2i" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,html,strapdown,lighttpd"

# Install the required software, namely Lighttpd and
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum install -y lighttpd  && \
    # clean yum cache files, as they are not needed and will only make the image bigger in the end
    yum clean all -y

# Although this is defined in openshift/base-centos7 image it's repeated here
# to make it clear why the following COPY operation is happening
LABEL io.openshift.s2i.scripts-url=image:///usr/libexec/sti
# Copy the S2I scripts from ./.sti/bin/ to /usr/libexec/sti
COPY ./.sti/bin/ /usr/libexec/sti

# Copy the lighttpd configuration file
COPY ./etc/ /opt/app-root/etc/
COPY ./assets/ /opt/app-root/assets/
RUN mkdir -p /opt/app-root/src

# Drop the root user and make the content of /opt/openshift owned by user 1001
RUN chown -R 1001:0 /opt/app-root

# Set the default user for the image, the user itself was created in the base image
USER 1001

# Specify the ports the final image will expose
EXPOSE 8080

# Set the default CMD to print the usage of the image, if somebody does docker run
CMD ["usage"]
