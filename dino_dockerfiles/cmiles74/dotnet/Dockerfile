FROM buildpack-deps:xenial-scm

run apt-get update
run apt-get install -y --no-install-recommends \
        build-essential automake libtool autogen

# install libuv
workdir /root
run wget https://github.com/libuv/libuv/archive/v1.4.2.tar.gz
run tar -zxvf v1.4.2.tar.gz
workdir /root/libuv-1.4.2
run sh /root/libuv-1.4.2/autogen.sh
run /root/libuv-1.4.2/configure
run make 
run make install
workdir /root
run rm -rf libuv-1.4.2
run rm -rf v1.4.2.tar.gz
run ldconfig

# install libicu
run wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-8ubuntu0.2_amd64.deb
run dpkg -i libicu52_52.1-8ubuntu0.2_amd64.deb

# Install .NET CLI dependencies
RUN apt-get install -y --no-install-recommends \
        libc6 \
        libcurl3 \
        libgcc1 \
        libgssapi-krb5-2 \
        libunwind8-dev \
        liblttng-ust0 \
        libssl1.0.0 \
        libstdc++6 \
        libunwind8 \
        libuuid1 \
        zlib1g \
    && rm -rf /var/lib/apt/lists/*

# Install .NET Core SDK
ENV DOTNET_SDK_VERSION 1.0.0-preview2-003156
ENV DOTNET_SDK_DOWNLOAD_URL https://dotnetcli.blob.core.windows.net/dotnet/preview/Binaries/$DOTNET_SDK_VERSION/dotnet-dev-debian-x64.$DOTNET_SDK_VERSION.tar.gz


RUN curl -SL $DOTNET_SDK_DOWNLOAD_URL --output dotnet.tar.gz \
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

