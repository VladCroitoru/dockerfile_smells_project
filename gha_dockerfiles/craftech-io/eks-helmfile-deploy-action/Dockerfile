FROM quay.io/roboll/helmfile:v0.135.0 as builder    

FROM craftech/ci-tools:kube-tools-latest

# Install the toolset.
RUN apk update \
    && apk add bash

# Copying helmfile binary and deploy.sh file
COPY --from=builder /usr/local/bin/helmfile /usr/local/bin/helmfile
COPY deploy.sh /usr/local/bin/deploy

ENTRYPOINT deploy