FROM soriyath/debian-swissfr:stretch
MAINTAINER Sumi Straessle

ENV DEBIAN_FRONTEND noninteractive
ENV DOTNET_SDK_VERSION 2.0.3
ENV DOTNET_SDK_DOWNLOAD_URL https://dotnetcli.blob.core.windows.net/dotnet/Sdk/$DOTNET_SDK_VERSION/dotnet-sdk-$DOTNET_SDK_VERSION-linux-x64.tar.gz
ENV DOTNET_SDK_DOWNLOAD_SHA 74A0741D4261D6769F29A5F1BA3E8FF44C79F17BBFED5E240C59C0AA104F92E93F5E76B1A262BDFAB3769F3366E33EA47603D9D725617A75CAD839274EBC5F2B

RUN set -ex \
  && apt-get update \
  && apt-get upgrade -y \
  && echo -e "nameserver 208.67.222.222\nnameserver 208.67.220.220\nnameserver 8.8.8.8\nnameserver 8.8.4.4" >> /etc/resolv.conf

# Install .NET CLI dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends --fix-missing \ 
        libc6 \
        libcurl3 \
        libgcc1 \
        libgssapi-krb5-2 \
        libicu57 \
        liblttng-ust0 \
        libssl1.1 \
        libstdc++6 \
        libunwind8 \
        libuuid1 \
        zlib1g

# Install .NET Core SDK
RUN curl -SL $DOTNET_SDK_DOWNLOAD_URL --output dotnet.tar.gz \
    && echo "$DOTNET_SDK_DOWNLOAD_SHA dotnet.tar.gz" | sha512sum -c - \
    && mkdir -p /usr/share/dotnet \
    && tar -zxf dotnet.tar.gz -C /usr/share/dotnet \
    && rm dotnet.tar.gz \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet

# Trigger the population of the local package cache
ENV NUGET_XMLDOC_MODE skip
RUN mkdir warmup \
    && cd warmup \
    && dotnet new \
    && cd .. \
    && rm -rf warmup \
    && rm -rf /tmp/NuGetScratch

RUN apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
