FROM ubuntu:16.04

# Install Dependencies
RUN echo "deb [arch=amd64] http://apt-mo.trafficmanager.net/repos/dotnet-release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893 \
    && apt-get update \
	&& apt-get install -y \
    curl \
    gettext \
    libunwind8 \
    libcurl4-openssl-dev \
    libicu-dev \
    libssl-dev \
    git \
    # .NET Core SDK
    dotnet-dev-1.0.1 \
 && rm -rf /var/lib/apt/lists/*

# Install mono
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF

RUN echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/4.2.3.4 main" > /etc/apt/sources.list.d/mono-xamarin.list \
	&& apt-get update \
	&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget \
	&& rm -rf /var/lib/apt/lists/*

# Install stable Node.js and related build tools
RUN curl -sL https://git.io/n-install | bash -s -- -ny - \
    && ~/n/bin/n stable \
    && npm install -g bower grunt gulp n \
    && rm -rf ~/n

# Prime dotnet
RUN mkdir dotnettest \
    && cd dotnettest \
    && dotnet new mvc --auth None --framework netcoreapp1.1 \
    && dotnet restore \
    && dotnet build \
    && cd .. \
    && rm -r dotnettest

# Display info installed components
RUN gulp --version
RUN npm --version
RUN mono --version
RUN dotnet --info