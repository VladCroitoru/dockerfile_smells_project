FROM alpine:3.14.2 AS binaries

ARG KUBECTL_VER="1.21.2"
ARG DOCKER_VER="20.10.9"
# upgrade to kind 0.10.0 held, as it defaults to kubernetes 1.20; we're still targeting primarly 1.19
ARG KIND_VER="0.11.1"
ARG APPTESTCTL_VER="0.12.0"

RUN apk add --no-cache ca-certificates curl \
    && mkdir -p /binaries \
    && curl -SL https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VER}/bin/linux/amd64/kubectl -o /binaries/kubectl \
    && curl -SL https://github.com/giantswarm/apptestctl/releases/download/v${APPTESTCTL_VER}/apptestctl-v${APPTESTCTL_VER}-linux-amd64.tar.gz | \
       tar -C /binaries --strip-components 1 -xvzf - apptestctl-v${APPTESTCTL_VER}-linux-amd64/apptestctl \
    && curl -SL https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VER}.tgz | \
       tar -C /binaries --strip-components 1 -xvzf - docker/docker \
    && curl -SL https://github.com/kubernetes-sigs/kind/releases/download/v${KIND_VER}/kind-linux-amd64 -o /binaries/kind

COPY container-entrypoint.sh /binaries

RUN chmod +x /binaries/*


FROM python:3.9.7-slim AS base

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    ATS_DIR="/ats" \
    PIPENV_VER="2020.11.15"

RUN pip install --no-cache-dir pipenv==${PIPENV_VER}

WORKDIR $ATS_DIR


FROM base as builder

# pip prerequesties
RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile.lock ./

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --clear


FROM base

ARG GO_VERSION="1.17.2"

ENV USE_UID=0 \
    USE_GID=0 \
    PATH="${ATS_DIR}/.venv/bin:/usr/local/go/bin:$PATH" \
    PYTHONPATH=$ATS_DIR \
    GOPATH=$ATS_DIR

# install dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl git sudo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -SL https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz | \
    tar -C /usr/local -xzf -

COPY --from=builder ${ATS_DIR}/.venv ${ATS_DIR}/.venv

COPY --from=binaries /binaries/* /usr/local/bin/

COPY app_test_suite/ ${ATS_DIR}/app_test_suite/

WORKDIR $ATS_DIR/workdir

# we assume the user will be using UID==1000 and GID=1000; if that's not true, we'll run `chown`
# in the container's startup script
RUN chown -R 1000:1000 $ATS_DIR

ENTRYPOINT ["container-entrypoint.sh"]

CMD ["-h"]
