FROM java:openjdk-8-jre

MAINTAINER Dale Peakall <dpeakall@thoughtworks.com>

ENV SONAR_SCANNER_MSBUILD_VERSION=4.0.2.892 \
    SONAR_SCANNER_VERSION=3.0.3.778 \
    SONAR_SCANNER_MSBUILD_HOME=/opt/sonar-scanner-msbuild \
    DOTNET_SKIP_FIRST_TIME_EXPERIENCE=true \
    DOTNET_CLI_TELEMETRY_OPTOUT=true \
    DOTNET_RUNTIME_VERSION=2.0.5 \
    DOTNET_SDK_VERSION=2.1.4

RUN set -x \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && echo "deb http://download.mono-project.com/repo/debian jessie main" | tee /etc/apt/sources.list.d/mono-official.list \
  && apt-get update \
  && apt-get install \
    curl \
    libunwind8 \
    gettext \
    apt-transport-https \
    mono-complete \
    ca-certificates-mono \
    referenceassemblies-pcl \
    mono-xsp4 \
    wget \
    unzip \
    jq \
    -y

RUN set - x \
  && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
  && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
  && curl https://packages.microsoft.com/config/debian/8/prod.list > prod.list \
  && mv prod.list /etc/apt/sources.list.d/microsoft-prod.list \
  && apt-get update \
  && apt-get install dotnet-host=$DOTNET_RUNTIME_VERSION-1 dotnet-hostfxr-$DOTNET_RUNTIME_VERSION dotnet-runtime-$DOTNET_RUNTIME_VERSION dotnet-sdk-$DOTNET_SDK_VERSION -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/$SONAR_SCANNER_MSBUILD_VERSION/sonar-scanner-msbuild-$SONAR_SCANNER_MSBUILD_VERSION.zip -O /opt/sonar-scanner-msbuild.zip \
  && mkdir -p $SONAR_SCANNER_MSBUILD_HOME \
  && unzip /opt/sonar-scanner-msbuild.zip -d $SONAR_SCANNER_MSBUILD_HOME \
  && rm /opt/sonar-scanner-msbuild.zip \
  && chmod 775 $SONAR_SCANNER_MSBUILD_HOME/*.exe \
  && chmod 775 $SONAR_SCANNER_MSBUILD_HOME/**/bin/* \
  && chmod 775 $SONAR_SCANNER_MSBUILD_HOME/**/lib/*.jar

ENV PATH="$SONAR_SCANNER_MSBUILD_HOME:$SONAR_SCANNER_MSBUILD_HOME/sonar-scanner-$SONAR_SCANNER_VERSION/bin:${PATH}"

RUN mkdir /opt/resource
COPY ./assets/* /opt/resource/
