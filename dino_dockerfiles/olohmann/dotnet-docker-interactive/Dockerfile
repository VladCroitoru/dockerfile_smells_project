FROM microsoft/dotnet:1.0.0-rc2-core-deps

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        vim \
    && rm -rf /var/lib/apt/lists/*

# Install .NET Core Latest
RUN curl -SL https://dotnetcli.blob.core.windows.net/dotnet/beta/Binaries/Latest/dotnet-debian-x64.latest.tar.gz --output dotnet.tar.gz \
    && mkdir -p /usr/share/dotnet \
    && tar -zxf dotnet.tar.gz -C /usr/share/dotnet \
    && rm dotnet.tar.gz \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet

# Install .NET Core SDK Latest
RUN curl -SL https://dotnetcli.blob.core.windows.net/dotnet/beta/Binaries/Latest/dotnet-dev-debian-x64.latest.tar.gz --output dotnet.sdk.tar.gz \
    && tar -zxf dotnet.sdk.tar.gz -C /usr/share/dotnet \
    && rm dotnet.sdk.tar.gz

# Alias for ls
RUN curl -SL https://gist.githubusercontent.com/olohmann/0d15f123d707bd9d3e6495f5e1e5a9bc/raw/5340d0a1a130df5d99dbd9615062371f6809eea8/bash-ls-alias --output tmp.alias \
    && cat tmp.alias >> $HOME/.bashrc \
    && rm tmp.alias
