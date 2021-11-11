# Copyright (c) 2021 Red Hat, Inc.
# Copyright Contributors to the Open Cluster Management project
FROM registry.ci.openshift.org/open-cluster-management/builder:nodejs14-linux as builder
USER root
COPY package.json package-lock.json ./
RUN npm ci
COPY ./backend ./backend
COPY ./frontend ./frontend
RUN npm run postinstall
RUN npm run build
RUN rm -rf backend/node_modules
RUN cd backend && npm ci --only=production --no-optional

FROM registry.access.redhat.com/ubi8/ubi-minimal
COPY --from=builder /usr/bin/node /usr/bin/node
RUN mkdir -p /app
WORKDIR /app
ENV NODE_ENV production
COPY --from=builder ./backend/node_modules ./node_modules
COPY --from=builder ./backend/build ./
COPY --from=builder ./frontend/build ./public

ARG VCS_REF
ARG VCS_URL
ARG IMAGE_NAME
ARG IMAGE_DESCRIPTION
ARG IMAGE_DISPLAY_NAME
ARG IMAGE_NAME_ARCH
ARG IMAGE_MAINTAINER
ARG IMAGE_VENDOR
ARG IMAGE_VERSION
ARG IMAGE_DESCRIPTION
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
    release="$VCS_REF" \
    description="$IMAGE_DESCRIPTION" \
    summary="$IMAGE_SUMMARY" \
    io.k8s.display-name="$IMAGE_DISPLAY_NAME" \
    io.k8s.description="$IMAGE_DESCRIPTION" \
    io.openshift.tags="$IMAGE_OPENSHIFT_TAGS"

RUN microdnf update &&\
    microdnf install ca-certificates vi --nodocs &&\
    microdnf clean all

USER 1001
EXPOSE 3000 4000
CMD ["node", "main.js"]