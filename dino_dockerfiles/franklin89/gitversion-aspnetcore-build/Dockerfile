FROM microsoft/aspnetcore-build:2.0

MAINTAINER Matteo Locher <matteo.locher@ml-software.ch>

# Install Mono
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && echo "deb http://download.mono-project.com/repo/debian wheezy-libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \
  && echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/4.4.2.11 main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \
  && apt-get update \
  && apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget referenceassemblies-pcl ncftp \
  && rm -rf /var/lib/apt/lists/*

# Install software for GitVersion
RUN echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots 4.4.2.11/main" | tee /etc/apt/sources.list.d/mono-xamarin.list \
  && echo "deb http://ftp.debian.org/debian sid main" | tee -a /etc/apt/sources.list \
  && apt-get clean && apt-get update \
  && apt-get install -y --no-install-recommends unzip git libc6 libc6-dev libc6-dbg libgit2-24 \
  && rm -rf /var/lib/apt/lists/* /tmp/* 

# Install GitVersion
RUN apt-get update && apt-get install -y unzip mono-runtime libmono-system-core4.0-cil libgit2-24 && \
    curl -L -o /tmp/GitVersion_4.0.0-beta0012.zip https://github.com/GitTools/GitVersion/releases/download/v4.0.0-beta.12/GitVersion_4.0.0-beta0012.zip && \
    unzip -d /opt/GitVersion /tmp/GitVersion_4.0.0-beta0012.zip && \
    rm /tmp/GitVersion_4.0.0-beta0012.zip && \
    echo '<configuration><dllmap os="linux" cpu="x86-64" wordsize="64" dll="git2-baa87df" target="/usr/lib/x86_64-linux-gnu/libgit2.so.24" /></configuration>' > \
    /opt/GitVersion/LibGit2Sharp.dll.config

RUN echo '#!/bin/bash\nexec mono /opt/GitVersion/GitVersion.exe "$@"' > /usr/bin/git-version

RUN chmod +x /usr/bin/git-version
