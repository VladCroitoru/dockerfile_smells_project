
# typescript-builder
FROM node:8-alpine

# TODO: Put the maintainer name in the image metadata
# MAINTAINER Your Name <your@email.com>

# TODO: Rename the builder environment variable to inform users about application you provide them
# ENV BUILDER_VERSION 1.0

# TODO: Set labels used in OpenShift to describe the builder image
LABEL io.k8s.description="Platform for building typescript" \
      io.k8s.display-name="builder typescript" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder" \
      io.openshift.s2i.destination="/tmp" \
      io.openshift.s2i.scripts-url="image:///usr/libexec/s2i"

# TODO: Install required packages here:
RUN yarn global add typescript
RUN apk add --update bash && rm -rf /var/cache/apk/*

# TODO (optional): Copy the builder files into /opt/app-root
# COPY ./<builder_folder>/ /opt/app-root/

# TODO: Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7 image
# sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./s2i/bin/ /usr/libexec/s2i

# TODO: Drop the root user and make the content of /opt/app-root owned by user 1001
RUN addgroup -g 1001 thenode && adduser -u 1001 -G thenode -s /bin/sh -D thenode
RUN chown -R 1001:1001 /home/thenode
RUN chown -R 1001:1001 /tmp

# TODO: Set the default port for applications built using this image
EXPOSE 8080

WORKDIR /home/thenode

USER 1001

# TODO: Set the default CMD for the image
CMD ["/usr/libexec/s2i/usage"]
