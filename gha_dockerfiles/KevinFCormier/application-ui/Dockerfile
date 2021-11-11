FROM registry.access.redhat.com/ubi8/nodejs-14:1

# Root needed for yum update, gets reset to 1001 below.
USER root
RUN yum -y remove nodejs-nodemon
RUN yum --nobest -y update

ARG VCS_REF
ARG VCS_URL
ARG IMAGE_NAME
ARG IMAGE_DESCRIPTION
ARG IMAGE_DISPLAY_NAME
ARG IMAGE_NAME_ARCH
ARG IMAGE_MAINTAINER
ARG IMAGE_VENDOR
ARG IMAGE_VERSION
ARG IMAGE_RELEASE
ARG IMAGE_SUMMARY
ARG IMAGE_OPENSHIFT_TAGS

LABEL org.label-schema.vendor="Red Hat" \
    org.label-schema.name="$IMAGE_NAME_ARCH" \
    org.label-schema.description="$IMAGE_DESCRIPTION" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url=$VCS_URL \
    org.label-schema.license="Red Hat Advanced Cluster Management for Kubernetes EULA" \
    org.label-schema.schema-version="1.0" \
    name="$IMAGE_NAME" \
    maintainer="$IMAGE_MAINTAINER" \
    vendor="$IMAGE_VENDOR" \
    version="$IMAGE_VERSION" \
    release="$IMAGE_RELEASE" \
    description="$IMAGE_DESCRIPTION" \
    summary="$IMAGE_SUMMARY" \
    io.k8s.display-name="$IMAGE_DISPLAY_NAME" \
    io.k8s.description="$IMAGE_DESCRIPTION" \
    io.openshift.tags="$IMAGE_OPENSHIFT_TAGS"

ENV BABEL_DISABLE_CACHE=1 \
    NODE_ENV=production \
    USER_UID=1001

RUN mkdir -p /opt/app-root/src/application-ui
WORKDIR /opt/app-root/src/application-ui

COPY .babelrc /opt/app-root/src/application-ui/.babelrc
COPY LICENSE /opt/app-root/src/application-ui/LICENSE
COPY app.js /opt/app-root/src/application-ui/app.js
COPY config /opt/app-root/src/application-ui/config
COPY controllers /opt/app-root/src/application-ui/controllers
COPY dll /opt/app-root/src/application-ui/dll
COPY fonts /opt/app-root/src/application-ui/fonts
COPY graphics /opt/app-root/src/application-ui/graphics
COPY lib /opt/app-root/src/application-ui/lib
COPY middleware /opt/app-root/src/application-ui/middleware
COPY nls /opt/app-root/src/application-ui/nls
COPY node_modules /opt/app-root/src/application-ui/node_modules
COPY public /opt/app-root/src/application-ui/public
COPY src-web /opt/app-root/src/application-ui/src-web
COPY templates /opt/app-root/src/application-ui/templates
COPY views /opt/app-root/src/application-ui/views

EXPOSE 3000

USER ${USER_UID}
CMD ["node", "app.js"]
