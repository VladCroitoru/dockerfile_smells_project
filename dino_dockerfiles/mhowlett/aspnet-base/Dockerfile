FROM ubuntu:14.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get -qq update \
    && apt-get -qqy install \
    automake \
    curl \
    gettext \
    libcurl3-dev \
    libssl-dev \
    libtool \
    libunwind8 \
    make \
    unzip \
    zlib1g \
    \
    && curl -sSL https://github.com/libuv/libuv/archive/v1.4.2.tar.gz | sudo tar zxfv - -C /usr/local/src \
    && cd /usr/local/src/libuv-1.4.2 \
    && sh autogen.sh \
    && ./configure \
    && make \
    && make install \
    && rm -rf /usr/local/src/libuv-1.4.2 && cd ~/ \
    && ldconfig

RUN mkdir /root/.config \
    && mkdir /root/.config/NuGet/ \
    && echo "<?xml version=\"1.0\" encoding=\"utf-8\"?>" >> /root/.config/NuGet/NuGet.config \
    && echo "<configuration>" >> /root/.config/NuGet/NuGet.config \
    && echo "  <packageSources>" >> /root/.config/NuGet/NuGet.config \
    && echo "    <add key=\"AspNetVNext\" value=\"https://www.myget.org/F/aspnetvnext/api/v2/\" />" >> /root/.config/NuGet/NuGet.config \
    && echo "    <add key=\"nuget.org\" value=\"https://www.nuget.org/api/v2/\" />" >> /root/.config/NuGet/NuGet.config \
    && echo "  </packageSources>" >> /root/.config/NuGet/NuGet.config \
    && echo "  <disabledPackageSources />" >> /root/.config/NuGet/NuGet.config \
    && echo "</configuration>" >> /root/.config/NuGet/NuGet.config

ENV DNX_VERSION 1.0.0-beta8
ENV DNX_USER_HOME /opt/dnx

RUN bash -c "curl -sSL https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.sh | DNX_USER_HOME=$DNX_USER_HOME DNX_BRANCH=v$DNX_VERSION sh \
   && source $DNX_USER_HOME/dnvm/dnvm.sh \
   && dnvm install $DNX_VERSION -a default -r coreclr \
   && dnvm alias default | xargs -i ln -s $DNX_USER_HOME/runtimes/{} $DNX_USER_HOME/runtimes/default"

ENV PATH $PATH:$DNX_USER_HOME/runtimes/default/bin