# Cloud9 server
# Inspired by https://github.com/sapk/dockerfiles/blob/master/cloud9/Dockerfile

FROM ubuntu:xenial
MAINTAINER Jonathan Camenzuli <jrcamenzuli@gmail.com>

RUN \
	buildDeps='make build-essential g++ gcc python2.7' \
	&& softDeps="tmux git curl wget openssh-server zip unzip imagemagick default-jre default-jdk vim" \
	&& apt-get update && apt-get upgrade -y \
	&& apt-get install -y $buildDeps $softDeps --no-install-recommends \
	&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \
	&& apt-get install -y nodejs \
	&& npm install -g forever && npm cache clean \
	&& git clone https://github.com/c9/core.git /cloud9 && cd /cloud9 \
	&& scripts/install-sdk.sh \
	&& apt-get clean -y \
	&& rm -rf /tmp/* /var/tmp/* \
	&& npm cache clean

# Install Leiningen / Clojure
ENV LEIN_ROOT true
ADD https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein /bin
RUN chmod a+x /bin/lein
RUN lein

# Install Rust
RUN \
	curl https://sh.rustup.rs > sh.rustup.rs && \
	chmod +x sh.rustup.rs && \
	./sh.rustup.rs -y && \
	rm sh.rustup.rs

# Install Go 1.8
RUN \
	wget https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz && \
	tar -C /usr/local -xzf go1.8.linux-amd64.tar.gz && \
	rm go1.8.linux-amd64.tar.gz && \
	echo "PATH=\$PATH:/usr/local/go/bin" >> /root/.bashrc

# Install Lua
RUN \
	wget https://downloads.sourceforge.net/project/luabinaries/5.3.3/Tools%20Executables/lua-5.3.3_Linux319_64_bin.tar.gz && \
	tar -C /bin -xzf lua-5.3.3_Linux319_64_bin.tar.gz && \
	rm lua-5.3.3_Linux319_64_bin.tar.gz

# Install Boost
WORKDIR /tmp
RUN wget https://dl.bintray.com/boostorg/release/1.64.0/source/boost_1_64_0.tar.gz && \
	tar -xzf boost_1_64_0.tar.gz && \
	mv /tmp/boost_1_64_0/boost /usr/include/
# Install Boost SIMD
RUN \
	git clone https://github.com/NumScale/boost.simd.git -b master && \
	mv boost.simd/include/boost/* /usr/include/boost

# Clean 
RUN rm -r /tmp/*

VOLUME /workspace
EXPOSE 8181 
ENTRYPOINT ["forever", "/cloud9/server.js", "-w", "/workspace", "-l", "0.0.0.0"]

#CMD["--auth","username:password"]

