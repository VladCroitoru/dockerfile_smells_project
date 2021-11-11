FROM amazonlinux:latest

WORKDIR /work
ADD . /work

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain stable && \
    PATH="/root/.cargo/bin:$PATH" rustup install stable && \
    PATH="/root/.cargo/bin:$PATH" rustup install nightly
RUN yum install -y bzip2-devel gcc gcc-c++ libgcc cmake wget git openssl-devel readline-devel sqlite-devel zip \
 && yum clean all

# Install node
RUN wget http://nodejs.org/dist/v8.10.0/node-v8.10.0.tar.gz && \
  tar -zxvf node-v8.10.0.tar.gz && \
  cd node-v8.10.0 && ./configure && make && \
  make install

RUN node -v
RUN npm i -g neon-cli
ENV PATH $PATH:/root/.cargo/bin

CMD ["/bin/bash"]