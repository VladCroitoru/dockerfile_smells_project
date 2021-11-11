FROM ubuntu:16.04

LABEL maintainer="Sayed Hadi Hashemi <hashemi3@illinois.edu>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        libcurl3-dev \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python-dev python3-dev \
        rsync \
        software-properties-common \
        unzip \
        zip \
        zlib1g-dev \
        openjdk-8-jdk \
        openjdk-8-jre-headless \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fSsL -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

RUN pip3 --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        scipy \
        sklearn \
        pandas \
        && \
    python3 -m ipykernel.kernelspec

# Set up Bazel.

# Running bazel inside a `docker build` command causes trouble, cf:
#   https://github.com/bazelbuild/bazel/issues/134
# The easiest solution is to set up a bazelrc file forcing --batch.
RUN echo "startup --batch" >>/etc/bazel.bazelrc
# Similarly, we need to workaround sandboxing issues:
#   https://github.com/bazelbuild/bazel/issues/418
RUN echo "build --spawn_strategy=standalone --genrule_strategy=standalone" \
    >>/etc/bazel.bazelrc
# Install the most recent bazel release.
ENV BAZEL_VERSION 0.5.4
WORKDIR /
RUN mkdir /bazel && \
    cd /bazel && \
    curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" -fSsL -O https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \
    curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" -fSsL -o /bazel/LICENSE.txt https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE && \
    chmod +x bazel-*.sh && \
    ./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \
    cd / && \
    rm -f /bazel/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh

# Download and build TensorFlow.

# RUN git clone https://github.com/tensorflow/tensorflow.git && \
#    cd tensorflow && \
#    git checkout r1.4
RUN git clone https://github.com/xldrx/tensorflow.git
WORKDIR /tensorflow

# TODO(craigcitro): Don't install the pip3 package, since it makes it
# more difficult to experiment with local changes. Instead, just add
# the built directory to the path.

ENV CI_BUILD_PYTHON python3

RUN tensorflow/tools/ci_build/builds/configured CPU \
    bazel build -c opt --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" \
        tensorflow/tools/pip_package:build_pip_package && \
    bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/pip3 && \
    pip3 --no-cache-dir install --upgrade /tmp/pip3/tensorflow-*.whl && \
    rm -rf /tmp/pip3
# Clean up pip3 wheel and Bazel cache when done.

# BUILD GRPC TensorFlow Server
RUN bazel build -c opt --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" \
        tensorflow/core/distributed_runtime/rpc:grpc_tensorflow_server && \
	ln -s `readlink -f /tensorflow/bazel-bin/tensorflow/core/distributed_runtime/rpc/grpc_tensorflow_server` /usr/bin/grpc_tensorflow_server

EXPOSE 2222

WORKDIR /root
CMD ["/usr/bin/grpc_tensorflow_server"]