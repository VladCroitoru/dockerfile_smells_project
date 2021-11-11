FROM jenkinsci/jnlp-slave:alpine
MAINTAINER Beni Ben Zikry

USER root

# Switch to root for build, avoid jenkins USER

ENV HELM_VERSION v2.8.1
ENV HELM_FILENAME helm-${HELM_VERSION}-linux-amd64.tar.gz

# Change this to your appropriate kube version
ENV KUBE_LATEST_VERSION="v1.8.4"

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=false \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8

# Enable detection of running in a container
ENV DOTNET_RUNNING_IN_CONTAINER=true \
# Set the invariant mode since icu_libs isn't included (see https://github.com/dotnet/announcements/issues/20)
    DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

# Install .NET Core SDK
ENV DOTNET_SDK_VERSION 2.1.301

# Enable correct mode for dotnet watch (only mode supported in a container)
ENV DOTNET_USE_POLLING_FILE_WATCHER=true \
# Skip extraction of XML docs - generally not useful within an image/container - helps perfomance
    NUGET_XMLDOC_MODE=skip



WORKDIR /

# .NET Core dependencies
RUN apk add --no-cache \
        ca-certificates \
        \
        krb5-libs \
        libgcc \
        libintl \
        libssl1.0 \
        libstdc++ \
        tzdata \
        userspace-rcu \
        zlib \
    && apk -X https://dl-cdn.alpinelinux.org/alpine/edge/main add --no-cache \
        lttng-ust

RUN apk add --update -t deps curl tar gzip ca-certificates git

RUN apk add --no-cache --virtual .build-deps \
    openssl \
    && wget -O dotnet.tar.gz https://dotnetcli.blob.core.windows.net/dotnet/Sdk/${DOTNET_SDK_VERSION}/dotnet-sdk-${DOTNET_SDK_VERSION}-linux-musl-x64.tar.gz \
    && dotnet_sha512='86e288cce53999b719ced7959f5ba652f667b8c1e0aec266c3012c9870380e5142e3f5ac103f03691d4426158d9da4d7c89f0739dee5815419a6150c8ee84a12' \
    && echo "$dotnet_sha512  dotnet.tar.gz" | sha512sum -c - \
    && mkdir -p /usr/share/dotnet \
    && tar -C /usr/share/dotnet -xzf dotnet.tar.gz \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet \
    && rm dotnet.tar.gz \
    && apk del .build-deps

# Trigger first run experience by running arbitrary cmd to populate local package cache
RUN dotnet help

RUN curl -L https://kubernetes-helm.storage.googleapis.com/helm-canary-linux-amd64.tar.gz | tar zxv -C /tmp \
  && cp /tmp/linux-amd64/helm /usr/local/bin/helm \
  && chmod +x /usr/local/bin/helm

# Install img
COPY ./installers/img.sh .
RUN chmod +x ./img.sh && ./img.sh && rm img.sh


# Install kubectl
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl

RUN apk del --purge deps \
 && rm /var/cache/apk/*

USER jenkins
RUN helm init --client-only
