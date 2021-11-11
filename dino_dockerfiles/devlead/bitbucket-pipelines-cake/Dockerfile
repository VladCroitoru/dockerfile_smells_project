FROM phusion/baseimage:0.9.19

# Install Dependencies
RUN apt-get update \
	&& apt-get install -y curl gettext libunwind8 libcurl4-openssl-dev libicu-dev libssl-dev git

# Install mono
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF

RUN echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/4.2.3.4 main" > /etc/apt/sources.list.d/mono-xamarin.list \
	&& apt-get update \
	&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget \
	&& rm -rf /var/lib/apt/lists/*



# Install .NET Core 
RUN mkdir -p /opt/dotnet \
    && curl -Lsfo /opt/dotnet/dotnet-install.sh https://raw.githubusercontent.com/dotnet/cli/rel/1.0.0/scripts/obtain/dotnet-install.sh \
    && bash /opt/dotnet/dotnet-install.sh --version 1.0.0-preview3-003223 --install-dir /opt/dotnet \
    && ln -s /opt/dotnet/dotnet /usr/local/bin
    

# Display info installed components
RUN mono --version
RUN dotnet --info

# Build Cake
RUN  curl -Lsfo caketools.tar.gz https://github.com/devlead/bitbucket-pipelines-cake/releases/download/v15.2/caketools.tar.gz \
    && mkdir -p /opt/caketools \
    && tar xzf caketools.tar.gz -C /opt/caketools --strip-components=1 tools
    
# Display Cake Version
RUN cd /opt/caketools/Cake && mono Cake.exe --version
