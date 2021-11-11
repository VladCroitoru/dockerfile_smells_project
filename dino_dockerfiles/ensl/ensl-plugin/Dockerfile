FROM ubuntu

# Need to install GCC-MULTILIB to be able to run amxxpc
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget git vim curl ca-certificates gcc-multilib hashalot unzip zip

RUN useradd -m amxx && mkdir -p /var/build/pkg && chown -R amxx:amxx /var/build

# Some paths
# /home/amxx/build - temporary copy
# /home/amxx/builD/base - Base AMXX files, not all included
# /home/amxx/build/pkg - result package
# /var/build - final product, mounted volume and copied on start

USER amxx

RUN mkdir -p /home/amxx/build/base /home/amxx/build/pkg /var/build
WORKDIR /home/amxx/build/base/

# Get all files and SHA-checkthem
RUN wget -q -O amxx.tgz "https://www.amxmodx.org/release/amxmodx-1.8.2-base-linux.tar.gz" && \
    wget -q -O amxx_ns.tgz "https://www.amxmodx.org/release/amxmodx-1.8.2-ns-linux.tar.gz" && \
    wget -q -O amxx.zip "https://www.amxmodx.org/release/amxmodx-1.8.2-base-windows.zip" && \
    wget -q -O amxx_ns.zip "https://www.amxmodx.org/release/amxmodx-1.8.2-ns-windows.zip" && \
    wget -q -O mm.zip "https://www.amxmodx.org/release/metamod-1.21.1-am.zip"

COPY files/amxmodx.sha /home/amxx/base/
# RUN sha256sum -c amxmodx.sha
# RUN sha256sum *.gz *.zip > /home/amxx/build/shasums

# Extract all package 
RUN yes|unzip -o amxx.zip && \
    yes|unzip -o amxx_ns.zip && \
    yes|unzip -o mm.zip && \
    tar -zxf amxx.tgz && \
    tar -zxf amxx_ns.tgz

# Copy build script, all AMXX source files and include files
COPY src/*.sma /home/amxx/build/base/addons/amxmodx/scripting/
COPY src/include/*  /home/amxx/build/base/addons/amxmodx/scripting/include

WORKDIR /home/amxx/build/base/addons/amxmodx/scripting

RUN mkdir -p /home/amxx/build/pkg/addons/amxmodx/plugins && \
    mkdir -p /home/amxx/build/pkg/addons/amxmodx/modules && \
    ./amxxpc ENSL.sma && \
    ./amxxpc extralevels3.sma && \
    ./amxxpc hiveccstatus.sma && \
    cp *.amxx /home/amxx/build/base/addons/amxmodx/plugins/ && \
    cp *.amxx /home/amxx/build

WORKDIR /home/amxx/build

# Then just copy the files we need. No extra.
RUN cp -rav base/addons/metamod pkg/addons/ && \
    cp -rav base/addons/amxmodx/modules pkg/addons/amxmodx/ && \
    cp -rav base/addons/amxmodx/plugins pkg/addons/amxmodx/ && \
    cp -rav base/addons/amxmodx/data pkg/addons/amxmodx/ && \
    cp -rav base/addons/amxmodx/dlls pkg/addons/amxmodx/ && \
    cp -rav base/addons/amxmodx/configs pkg/addons/amxmodx/

# Copy ENSL to its place, add overlay files and zip the whole thing
RUN cp ENSL.amxx pkg/addons/amxmodx/plugins/
ADD pkg /home/amxx/build/pkg

RUN cd pkg && zip -9 -r ENSL_SrvPkg.zip * && mv ENSL_SrvPkg.zip ..

COPY build.sh /home/amxx/

USER root
ENTRYPOINT ["/bin/bash", "/home/amxx/build.sh"]
