FROM ubuntu:xenial
MAINTAINER David Spencer <dspencer@wustl.edu>

LABEL Image for tumor/normal concordance check

#some basic tools
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
    bzip2 \
    curl \
    default-jdk \
    default-jre \
    g++ \
    git \
    less \
    libcurl4-openssl-dev \
    libpng-dev \
    libssl-dev \
    libxml2-dev \
    make \
    ncurses-dev \
    nodejs \
    pkg-config \
    python \
    python-dev \
    virtualenv \
    python-pip \
    rsync \
    unzip \
    wget \
    zip \
    zlib1g-dev \
    bc \
    tzdata

# needed for MGI data mounts
RUN apt-get update && apt-get install -y libnss-sss && apt-get clean all

#set timezone to CDT
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime
#LSF: Java bug that need to change the /etc/timezone.
#     The above /etc/localtime is not enough.
RUN echo "America/Chicago" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# some other utils
RUN apt-get update && apt-get install -y --no-install-recommends gawk openssh-client grep evince && apt-get clean all

##############
#Picard
##############
ENV picard_version 2.8.1

# Assumes Dockerfile lives in root of the git repo. Pull source files into
# container
RUN apt-get update && apt-get install ant --no-install-recommends -y && \
    cd /usr/ && \
    git config --global http.sslVerify false && \
    git clone --recursive https://github.com/broadinstitute/picard.git && \
    cd /usr/picard && \
    git checkout tags/${picard_version} && \
    ./gradlew shadowJar && \
    cp ./build/libs/picard.jar .
    
##########
#GATK 3.6#
##########
ENV maven_package_name apache-maven-3.3.9
ENV gatk_dir_name gatk-protected
ENV gatk_version 3.6
RUN cd /tmp/ && wget -q http://mirror.nohup.it/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.zip

# LSF: Comment out the oracle.jrockit.jfr.StringConstantPool.
RUN cd /tmp/ \
    && git clone --recursive https://github.com/broadgsa/gatk-protected.git \
    && cd /tmp/gatk-protected && git checkout tags/${gatk_version} \
    && sed -i 's/^import oracle.jrockit.jfr.StringConstantPool;/\/\/import oracle.jrockit.jfr.StringConstantPool;/' ./public/gatk-tools-public/src/main/java/org/broadinstitute/gatk/tools/walkers/varianteval/VariantEval.java \
    && mv /tmp/gatk-protected /opt/${gatk_dir_name}-${gatk_version}
RUN cd /opt/ && unzip /tmp/${maven_package_name}-bin.zip \
    && rm -rf /tmp/${maven_package_name}-bin.zip LICENSE NOTICE README.txt \
    && cd /opt/ \
    && cd /opt/${gatk_dir_name}-${gatk_version} && /opt/${maven_package_name}/bin/mvn verify -P\!queue \
    && mv /opt/${gatk_dir_name}-${gatk_version}/protected/gatk-package-distribution/target/gatk-package-distribution-${gatk_version}.jar /opt/GenomeAnalysisTK.jar \
    && rm -rf /opt/${gatk_dir_name}-${gatk_version} /opt/${maven_package_name}
    
