# Copyright Contributors to the Open Cluster Management project

FROM registry.access.redhat.com/ubi8/nodejs-14:1 as builder

USER root
RUN yum install git python2 -y

RUN mkdir -p /opt/app-root/src/grc-ui
WORKDIR /opt/app-root/src/grc-ui

COPY . .

RUN make install
RUN make build-prod
RUN make prune

FROM registry.ci.openshift.org/open-cluster-management/common-nodejs-parent:nodejs-14
RUN microdnf update
RUN mkdir -p /opt/app-root/src/grc-ui
WORKDIR /opt/app-root/src/grc-ui

COPY --from=builder /opt/app-root/src/grc-ui /opt/app-root/src/grc-ui

ENV BABEL_DISABLE_CACHE=1 \
    NODE_ENV=production \
    USER_UID=1001

EXPOSE 3000

USER ${USER_UID}
CMD ["node", "app.js"]
