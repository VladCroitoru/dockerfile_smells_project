FROM google/cloud-sdk:alpine

MAINTAINER Chris Every <eversmcc@gmail.com>

RUN apk update && apk add ca-certificates && apk add openssl && rm -rf /var/cache/apk/*

ENV HELM_VERSION v2.9.0
ENV HELM_GCS_PLUGIN_VERSION 0.2.1

RUN adduser -S gkh gkh

RUN gcloud components install docker-credential-gcr -q --no-user-output-enabled
RUN gcloud components install kubectl -q --no-user-output-enabled
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > get_helm.sh
RUN chmod 700 get_helm.sh
RUN ./get_helm.sh --version $HELM_VERSION
RUN mkdir helm-bulk-plugin
ENV HELM_HOME /home/gkh/.helm/

USER gkh

RUN helm init --client-only
RUN helm plugin install https://github.com/hayorov/helm-gcs --version $HELM_GCS_PLUGIN_VERSION
RUN helm plugin install https://github.com/ovotech/helm-bulk
