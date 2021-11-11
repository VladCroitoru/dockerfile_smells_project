FROM ubuntu:16.04

# Install Dependencies
RUN apt-get update \
	&& apt-get install -y curl gettext libunwind8 libcurl4-openssl-dev libicu-dev libssl-dev git apt-transport-https build-essential

# Install mono
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
    && echo "deb http://download.mono-project.com/repo/ubuntu xenial main" > /etc/apt/sources.list.d/mono-official.list \
    && apt-get update \
    && apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget \
    && rm -rf /var/lib/apt/lists/*

# Install .NET Core and Nuget
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EB3E94ADBE1229CF \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list \
    && apt-get update \
    && apt-get install -y dotnet-sdk-2.0.2 \
    && mkdir -p /opt/dotnet \
    && ln -s /opt/dotnet/dotnet /usr/local/bin \
    && mkdir -p /opt/nuget \
    && curl -Lsfo /opt/nuget/nuget.exe https://dist.nuget.org/win-x86-commandline/latest/nuget.exe

# Prime dotnet
RUN mkdir dotnettest \
    && cd dotnettest \
    && dotnet new console \
    && dotnet restore \
    && dotnet build \
    && cd .. \
    && rm -r dotnettest

# Install Node.js 7.x repository and Autorest
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g autorest \
    && autorest --latest

COPY . /app
WORKDIR /app

ENTRYPOINT /bin/bash

