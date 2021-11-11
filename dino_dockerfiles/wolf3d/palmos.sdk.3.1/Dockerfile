# Pull base image
FROM wolf3d/debian.4.0-etch

RUN echo "deb http://archive.debian.org/debian/ etch main non-free contrib" > /etc/apt/sources.list && \
apt-get update && apt-get install -y vim less tar cogito git-core curl && \
cd /root && git clone git://github.com/wolf3d/debian-scripts && cd debian-scripts && \
chmod +x ./setup-palmos-sdk && ./setup-palmos-sdk

CMD ["/bin/bash"]
