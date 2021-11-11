FROM centos:7

MAINTAINER AlexLee <alexlee7171@gmail.com>

RUN yum update -y
RUN yum install -y gcc gcc-c++ openssl-devel mariadb-devel git make wget unzip tmux

# Download Source Code
RUN git clone https://github.com/kbengine/kbengine.git

# Download Demo Code
RUN cd /kbengine && git clone https://github.com/kbengine/kbengine_cocos2d_js_demo.git && \
	cd /kbengine/kbengine_cocos2d_js_demo && git submodule update --init --remote && \
	cp -a /kbengine/kbengine_cocos2d_js_demo/kbengine_demos_assets /kbengine

ADD kbengine_defs.xml /kbengine/kbe/res/server/kbengine_defs.xml

RUN chmod -R 777 /kbengine

WORKDIR /kbengine/kbe/src

RUN make

# Define mountable directories.
VOLUME ["/kbengine"]

# Create user : kbe
RUN groupadd -r kbe && useradd -r -g kbe kbe

WORKDIR /kbengine/kbengine_demos_assets

RUN ./start_server.sh

WORKDIR /kbengine/kbengine_cocos2d_js_demo/cocos2d-js-client

CMD ["python", "-m", "SimpleHTTPServer", "80"]

EXPOSE 80
EXPOSE 20013
