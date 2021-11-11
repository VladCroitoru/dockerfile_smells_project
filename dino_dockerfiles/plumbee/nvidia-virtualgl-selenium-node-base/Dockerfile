FROM selenium/base:3.0.1-dysprosium

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

#===================
# Timezone settings
# Possible alternative: https://github.com/docker/docker/issues/3359#issuecomment-32150214
#===================
ENV TZ "US/Pacific"
RUN echo "${TZ}" > /etc/timezone \
  && dpkg-reconfigure --frontend noninteractive tzdata

#==============================
# install VirtualGl
# see https://github.com/plumbee/nvidia-virtualgl
#==============================
ENV VIRTUALGL_VERSION 2.5.2
RUN apt-get update && apt-get install -y \
    libglu1-mesa-dev mesa-utils wget xterm && \
    wget http://downloads.sourceforge.net/project/virtualgl/${VIRTUALGL_VERSION}/virtualgl_${VIRTUALGL_VERSION}_amd64.deb && \
    dpkg -i virtualgl*_amd64.deb  &&\
    /opt/VirtualGL/bin/vglserver_config -config +s +f -t && \
    rm virtualgl*_amd64.deb && \
    apt-get remove -y wget && \
    rm -rf /var/lib/apt/lists/*

# nvidia-docker links
LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV PATH /usr/local/nvidia/bin:/opt/VirtualGL/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}

#==============================
# Scripts to run Selenium Node
#==============================
COPY \
  entry_point.sh \
    /opt/bin/
RUN chmod +x /opt/bin/entry_point.sh

#============================
# Some configuration options
#============================
#TODO: maybe inject these? are these ever used by Selenium?
ENV SCREEN_WIDTH 1360
ENV SCREEN_HEIGHT 1020
ENV SCREEN_DEPTH 24

USER seluser

CMD ["/opt/bin/entry_point.sh"]
