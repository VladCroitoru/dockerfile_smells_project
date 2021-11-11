FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

# RETDEC
RUN apt-get update
RUN apt-get install -y build-essential cmake git openssl libssl-dev python3 autoconf automake libtool pkg-config m4 zlib1g-dev upx doxygen graphviz ssh openssh-server gdb libcapstone-dev libcapstone3 rapidjson-dev
WORKDIR /retdec
RUN wget https://github.com/avast/retdec/releases/download/v4.0/retdec-v4.0-ubuntu-64b.tar.xz
RUN tar -xf retdec-v4.0-ubuntu-64b.tar.xz
WORKDIR /retdec/retdec
RUN cp -r ./bin/* /usr/local/bin/
RUN cp -r ./include/* /usr/local/include/
RUN cp -r ./lib/* /usr/local/lib/
RUN cp -r ./share/* /usr/local/share/

# CROSSMATCH
WORKDIR /app
COPY src src/
COPY include include/
COPY samples samples/
COPY CMakeLists.txt .
COPY config.json .
RUN cmake -G "Unix Makefiles" .
RUN make -j 6

# TOOLS
RUN apt-get install vim -y

# DEBUG
RUN sed -ri 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/' /etc/ssh/sshd_config
RUN sed -ri 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config
RUN passwd -d root
RUN /etc/init.d/ssh start

CMD ["/usr/sbin/sshd", "-D"]
