# SPDX-License-Identifier: Apache-2.0
FROM python:3.9-alpine

ARG VERSION="local"
ARG REVISION="none"
ARG GITHUB_WORKFLOW="none"
ARG GITHUB_RUN_ID="none"

RUN apk upgrade --update-cache -a && \
    apk add --no-cache \
    git \
    nodejs
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY common common

EXPOSE 8000

# Build doc by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr", "0.0.0.0:8000"]

# Labels
LABEL org.opencontainers.image.title="ConsenSys Doctools builder image."
LABEL org.opencontainers.image.description="Docker image to build (locally or with CI) and preview ConsenSys documentation websites while writing."
LABEL org.opencontainers.image.url="https://github.com/ConsenSys/doctools.action-builder"
LABEL org.opencontainers.image.documentation="https://consensys.net/docs/doctools/en/latest/howto/advanced/contributing/"
LABEL org.opencontainers.image.source="https://github.com/ConsenSys/doctools.action-builder"
LABEL org.opencontainers.image.version=${VERSION}
LABEL org.opencontainers.image.revision=${REVISION}
LABEL org.opencontainers.image.vendor="ConsenSys"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL github.workflow=${GITHUB_WORKFLOW}
LABEL github.runid=${GITHUB_RUN_ID}
