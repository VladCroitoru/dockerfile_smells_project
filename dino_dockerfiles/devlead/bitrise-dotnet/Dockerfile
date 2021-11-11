FROM bitriseio/docker-bitrise-base:latest

# Install .NET Core & mono & nuget
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
    && echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/5.10 main" > /etc/apt/sources.list.d/mono-xamarin.list \
    && wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb \
    && sudo dpkg -i packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install -y apt-transport-https dos2unix libcurl4-openssl-dev libunwind8 \
    && apt-get update \
    && apt-get install -y --no-install-recommends dotnet-sdk-2.1  \
	&& apt-get install -y --no-install-recommends unzip mono-devel \
	&& rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && mkdir -p /opt/nuget \
    && curl -Lsfo /opt/nuget/nuget.exe https://dist.nuget.org/win-x86-commandline/latest/nuget.exe

ENV PATH "$PATH:/opt/nuget"

# Prime dotnet
RUN mkdir dotnettest \
    && cd dotnettest \
    && dotnet new console -lang C# \
    && dotnet restore \
    && dotnet build \
    && dotnet run \
    && cd .. \
    && rm -r dotnettest

# Prime Integration tests & Cake
ADD integrationtestprimer integrationtestprimer
ADD cakeprimer cakeprimer
RUN cd integrationtestprimer \
    && dotnet restore hwapp.sln \
    --source "https://api.nuget.org/v3/index.json" \
    && cd .. \
    && rm -rf integrationtestprimer \
    && cd cakeprimer \
    && dotnet restore Cake.sln \
    --source "https://api.nuget.org/v3/index.json" \
    && cd .. \
    && rm -rf cakeprimer

# Get & Test Cake
ENV CAKE_VERSION 0.30.0
ENV CAKE_SETTINGS_SKIPVERIFICATION true
ADD cake /usr/bin/cake
RUN dos2unix -q /usr/bin/cake \
    && mkdir -p /opt/Cake/Cake \
    && curl -Lsfo Cake.zip "https://www.nuget.org/api/v2/package/Cake/$CAKE_VERSION" \
    && unzip -q Cake.zip -d "/opt/Cake/Cake" \
    && rm -f Cake.zip \
    && chmod 755 /usr/bin/cake \
    && sync \
    && mkdir caketest \
    && cd caketest \
    && cake --version \
    && cd .. \
    && rm -rf caketest

# Display info installed components
RUN mono --version \
    && dotnet --info \
    && mono /opt/nuget/nuget.exe help \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*