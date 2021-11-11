FROM jetbrains/teamcity-agent:latest

MAINTAINER Dmitry Shultz <dmitry@diligesoft.com>

ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/zeppelinux/teamcity-agent-with-helm" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.docker.dockerfile="/Dockerfile"

RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > get_helm.sh \
 && chmod 700 get_helm.sh \
 && ./get_helm.sh