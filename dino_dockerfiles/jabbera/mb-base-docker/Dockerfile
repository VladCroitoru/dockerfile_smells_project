# Mediabrowser base includes all dependencies to make rebuilding the main mediabrowser image faster
FROM ubuntu:14.04
MAINTAINER Jacob Alberty <jacob.alberty@gmail.com>

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Set locale to UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN dpkg-reconfigure locales


# Add keys
## MediaBrowser
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 637D1286 && \
    echo 'deb http://ppa.launchpad.net/apps-z/mediabrowser/ubuntu trusty main' > /etc/apt/sources.list.d/20mediabrowser.list
## Mono
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo 'deb http://download.mono-project.com/repo/debian wheezy/snapshots/3.10.0 main' > /etc/apt/sources.list.d/mono-xamarin.list && \
    echo 'deb http://download.mono-project.com/repo/debian wheezy-apache24-compat main' >> etc/apt/sources.list.d/mono-xamarin.list
RUN apt-get -q update && \
    apt-get install -qy \
        mono-runtime libmediainfo0 libmono-corlib2.0-cil libmono-corlib4.5-cil libmono-microsoft-csharp4.0-cil \
        libmono-posix4.0-cil libmono-security4.0-cil libmono-sharpzip2.84-cil libmono-system-configuration4.0-cil \
        libmono-system-core4.0-cil libmono-system-data-linq4.0-cil libmono-system-data2.0-cil libmono-system-data4.0-cil \
        libmono-system-drawing4.0-cil libmono-system-runtime-serialization4.0-cil libmono-system-servicemodel4.0a-cil \
        libmono-system-transactions4.0-cil libmono-system-web4.0-cil libmono-system-windows-forms4.0-cil \
        libmono-system-xml-linq4.0-cil libmono-system-xml4.0-cil libmono-system2.0-cil libmono-system4.0-cil libsqlite3-0 \
        libwebp5 mono-devel libsqlite3-dev sqlite3 && \
   apt-get -q clean && \
    rm -rf /var/lib/apt/lists/*
