FROM jetbrains/teamcity-agent:2017.2
LABEL maintainer="mkordi@gmail.com"

#Known issue:
# tzdata should be installed or nuget fails to download.

# Install Mono + tzdata
RUN apt-get update \
&&  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
&&  echo "deb http://download.mono-project.com/repo/ubuntu xenial main" > /etc/apt/sources.list.d/mono-official.list \
&&  apt-get update \
&&  apt-get install -y mono-devel \
&&  apt-get install -y tzdata

# Install dotnet
RUN apt-get update \ 
&&  apt-get install apt-transport-https \
&& curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
&& mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
&& echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list \
&&  apt-get update \
&&  apt-get install -y dotnet-sdk-2.1

COPY build.bootstrap.csproj .build/bootsrap.csproj

RUN dotnet restore .build/bootsrap.csproj \
&& echo "#!/bin/bash" > /usr/local/bin/fake \
&& echo "mono ~/.nuget/packages/fake/4.61.3/tools/FAKE.exe \"\$@\"" >> /usr/local/bin/fake \
&& chmod +x /usr/local/bin/fake

# Install nodejs and npm
RUN apt-get update \
&&  curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
&&  add-apt-repository "deb https://deb.nodesource.com/node_6.x xenial main" \
&&  apt-get update \
&&  apt-get install -y --allow-unauthenticated nodejs

# Install yarn
RUN apt-get update \
&&  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
&&  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
&&  apt-get update \
&&  apt-get install -y yarn \
&&  apt-get clean all

# Install docker
RUN apt-get update \ 
&&  apt-get install -y apt-transport-https \
&&  apt-get install -y curl \
&&  apt-get install -y software-properties-common \
&&  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
&&  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" \
&&  apt-get install -y docker \
&&  apt-get clean all

# expose environment variables
ENV tool_dotnetcore=2.1
ENV tool_mono=5.4.1.6
ENV tool_fake=4.61.3
ENV tool_node=6.14.2
ENV tool_yarn=1.7.0