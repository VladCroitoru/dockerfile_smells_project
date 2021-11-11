FROM java:openjdk-8-jdk
MAINTAINER Shawn Dempsay <sdempsay@pavlovmedia.com>

# Upgrade
RUN apt-get update && apt-get upgrade -y

# Moqui Framework
ENV "moqui_framework_version" "master"
RUN echo ${moqui_framework_version}

ADD "https://github.com/moqui/moqui-framework/archive/${moqui_framework_version}.zip" "moqui-framework.zip"
RUN unzip moqui-framework.zip -d /opt

# Moqui Runtime
WORKDIR /opt/moqui-framework-${moqui_framework_version}
RUN ./gradlew getRuntime

# Moqui - HiveMind
RUN ./gradlew getCurrent -Pcomponent=HiveMind

# Moqui - PopCommerce
RUN ./gradlew getCurrent -Pcomponent=PopCommerce

# Moqui - AuthorizeDotNet
RUN ./gradlew getCurrent -Pcomponent=AuthorizeDotNet

# Moqui - mantle-ubpl
RUN ./gradlew getComponent -Pcomponent=mantle-ubpl

# Moqui - moqui-kie
RUN ./gradlew getComponent -Pcomponent=moqui-kie

# Run Moqui
CMD ./gradlew build load run
