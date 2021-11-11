FROM ubuntu:18.04

# Install Dependencies
RUN apt-get update \
	&& apt-get install -y curl gettext libunwind8 libcurl4-openssl-dev libicu-dev libssl-dev git apt-transport-https

# Install mono
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | tee /etc/apt/sources.list.d/mono-official-stable.list \
	&& apt-get update \
	&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget \
	&& rm -rf /var/lib/apt/lists/*

# Install .NET Core
RUN curl -Lsf "https://packages.microsoft.com/keys/microsoft.asc" | gpg --dearmor > microsoft.asc.gpg \
	&& mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/ \
	&& curl -LsfO "https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb" \
	&& dpkg -i packages-microsoft-prod.deb \
	&& apt-get update \
	&& apt-get install -y dotnet-sdk-2.1 \
	&& mkdir -p /opt/dotnet \
	&& ln -s /opt/dotnet/dotnet /usr/local/bin

# Install NuGet
RUN mkdir -p /opt/nuget \
    && curl -Lsfo /opt/nuget/nuget.exe https://dist.nuget.org/win-x86-commandline/latest/nuget.exe

# Prime dotnet
RUN mkdir dotnettest \
    && cd dotnettest \
    && dotnet new console \
    && dotnet restore \
    && dotnet build \
    && cd .. \
    && rm -r dotnettest

# Display info installed components
RUN mono --version
RUN dotnet --info
