FROM microsoft/vsts-agent:ubuntu-16.04-docker-17.03.0-ce

# Install packages
RUN echo "deb [arch=amd64] http://apt-mo.trafficmanager.net/repos/dotnet-release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list \
 && apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    apt-transport-https \
    # locales
    locales \
    # Basic utilities
    curl \
    dnsutils \
    ftp \
    iproute2 \
    iputils-ping \
    openssh-client \
    sudo \
    telnet \
    time \
    unzip \
    wget \
    zip \
    # Essential build tools (gcc, make, etc.)
    build-essential \
    # Python
    python \
    python3 \
    python-pip \
    python-setuptools \
    python-dev \
    python3-dev \
    # Java and related build tools
    openjdk-8-jdk \
    ant \
    ant-optional \
    ruby \
    ruby-dev \
    libxml2-dev \
    libxslt-dev \
    zlib1g-dev \
    nmap \
    golang \
    # .NET Core SDK
    dotnet-dev-1.0.1 \
 && rm -rf /var/lib/apt/lists/*

# Setup locale
RUN locale-gen en_US.UTF-8 \
  && echo "LANG=en_US.UTF-8" >> /etc/default/locale

ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

# Install maven separately to avoid apt-get errors
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    maven \
 && rm -rf /var/lib/apt/lists/*

# Install gradle separately to avoid apt-get errors
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    gradle \
 && rm -rf /var/lib/apt/lists/*

# Install stable Node.js and related build tools
RUN curl -sL https://git.io/n-install | bash -s -- -ny - \
 && ~/n/bin/n stable \
 && npm install -g bower grunt gulp n \
 && rm -rf ~/n

 # Install MS SQL command line tools
 RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list \
  && apt-get update -y \
  && ACCEPT_EULA=Y apt-get install mssql-tools unixodbc-dev -y \
  && rm -rf /var/lib/apt/lists/*

# Configure environment variables
ENV ANT_HOME=/usr/share/ant \
    bower=/usr/local/bin/bower \
    dotnet=/usr/bin/dotnet \
    GRADLE_HOME=/usr/share/gradle \
    grunt=/usr/local/bin/grunt \
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    M2_HOME=/usr/share/maven \
    GOPATH=/go \
    chef=/usr/bin/chef

# Install gauntlt, arachni
RUN gem install gauntlt arachni --no-ri

# Configure go bin path
ENV PATH=$PATH:/go/bin

# Install heartbleed
RUN /usr/bin/go get github.com/FiloSottile/Heartbleed

# Install sslyze, and sqlmap
RUN pip install --upgrade pip
RUN pip install sqlmap
RUN pip install sslyze

# Install Chef
RUN curl -L https://omnitruck.chef.io/install.sh | sudo bash -s -- -P chefdk -v 1.2.22
ENV CHEFDK=1.2.22

# Add gems for chef
COPY Gemfile Gemfile
RUN chef exec bundle install && rm -f Gemfile

# Diable telemetry
ENV DOTNET_CLI_TELEMETRY_OPTOUT=1

# Forces first run which downloads and unpacks some stuff.
RUN /usr/bin/dotnet msbuild /version

# Setup MSbuild alias (remove once we have this natively)
RUN echo "alias msbuild='dotnet msbuild'" >> /etc/bash.bashrc
