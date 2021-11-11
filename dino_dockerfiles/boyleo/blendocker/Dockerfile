FROM nvidia/cuda

LABEL authors="Boonsak Watanavisit"

ENV VIRTUALGL_VERSION 2.5.2

# install VirtualGL 
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglu1-mesa-dev mesa-utils curl ca-certificates xterm && \
    curl -sSL https://downloads.sourceforge.net/project/virtualgl/"${VIRTUALGL_VERSION}"/virtualgl_"${VIRTUALGL_VERSION}"_amd64.deb -o virtualgl_"${VIRTUALGL_VERSION}"_amd64.deb && \
    dpkg -i virtualgl_*_amd64.deb && \
    /opt/VirtualGL/bin/vglserver_config -config +s +f -t && \
    rm virtualgl_*_amd64.deb

RUN apt-get install -y blender

ENV BLENDER_MAJOR 2.78
ENV BLENDER_VERSION 2.78c
ENV BLENDER_BZ2_URL http://ftp.halifax.rwth-aachen.de/blender/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-linux-glibc219-x86_64.tar.bz2

RUN mkdir /usr/local/blender && \
	curl -SL "$BLENDER_BZ2_URL" -o blender.tar.bz2 && \
	tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1 && \
	rm blender.tar.bz2

RUN apt-get clean && \
    apt-get remove -y curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# nvidia-docker links
LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV PATH /usr/local/nvidia/bin:/opt/VirtualGL/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH} 


VOLUME /media
ENTRYPOINT ["/usr/local/blender/blender"]
