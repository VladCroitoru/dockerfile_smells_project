#WOLFENSTEIN DOCKERFILE
#docker build --tag wolf3d .
#docker run -it --name runner wolf3d
#If you want to run the container, use
#docker start -i runner
FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive
ENV LD_LIBRARY_PATH "/usr/local/lib"
RUN apt-get update -y && \
	apt-get upgrade -y && \
	apt-get install sudo gcc build-essential valgrind vim libxkbcommon-dev xorg wayland-protocols -y
COPY . wolfenstein3d/
RUN cd wolfenstein3d && make
ENTRYPOINT /wolfenstein3d/wolf3d map_files/map.TEST
