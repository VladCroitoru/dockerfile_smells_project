FROM alpine:latest


RUN apk update && \

    # Project dependencies
    apk add g++ \
            cmake \
            ninja \
            gtest \
            gtest-dev \
            protobuf \
            protobuf-dev \

            # gRPC compilation dependencies
            gcc \
            make \
            automake \
            autoconf \
            libtool \
            openssl-dev \
            libffi-dev \
            git \
            curl \

            # Cpp-Coveralls dependencies
            python3 \
            python3-dev \
            py2-pip



# Cpp Coveralls installation
RUN pip3 install pip --upgrade
RUN pip3 install PyOpenSSL --upgrade
RUN pip3 install cpp-coveralls



RUN mkdir -pv /vetulus
ADD . /vetulus/
WORKDIR /vetulus



RUN /vetulus/scripts/install_deps.sh
RUN /vetulus/scripts/compile.sh


EXPOSE 4242


CMD /vetulus/scripts/run_docker.sh
