FROM ubuntu:20.04 AS base
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y tzdata gnupg gnupg-utils lsb-release wget ca-certificates apt-transport-https
ENTRYPOINT ["/bin/bash"]

# Auxiliary container to build RGIS
FROM base AS rgis
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends git cmake clang curl make libnetcdf-dev libudunits2-dev \
            libgdal-dev libexpat1-dev libxext-dev libmotif-dev
RUN git clone https://github.com/bmfekete/RGIS /tmp/RGIS && /tmp/RGIS/install.sh /usr/local/share && rm -rf /tmp/RGIS
ENV PATH="${PATH}:/usr/local/share/ghaas/bin:/usr/local/share/ghaas/f"

# Minimum container with basic command-line applications
FROM base AS compute
RUN apt-get install -y --no-install-recommends dialog apt-utils apt-transport-https dnsutils psmisc \
            vim rsync screen tmux bc curl nfs-common python python-numpy python-psutil gnuplot imagemagick \
            netcdf-bin nco cdo libudunits2-0 libudunits2-data gdal-bin python-gdal python3-gdal \
            postgresql-client-common libexpat1 libmotif-common libxss1 && rm -rf /var/lib/apt/lists/*
   COPY --from=rgis /usr/local/share/ghaas /usr/local/share/ghaas
   ENV PATH=\"${PATH}:/usr/local/share/ghaas/bin:/usr/local/share/ghaas/f\"

# Container with basic command-line and desktop applications
FROM compute AS desktop
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y xbase-clients xfonts-100dpi xfonts-100dpi-transcoded xfonts-75dpi xfonts-75dpi-transcoded \
            xrdp xfce4 xfce4-goodies qgis && rm -rf /var/lib/apt/lists/*