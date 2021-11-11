FROM tensorflow/tensorflow:1.2.1-devel-gpu

MAINTAINER Jung Kwon Lee <jklee@sktbrain.com>

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
ENV BAZEL_VERSION 0.5.0
WORKDIR /
#RUN mkdir /bazel && \
RUN cd /bazel && \
  curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" -fSsL -O https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \
  curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" -fSsL -o /bazel/LICENSE.txt https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE && \
  chmod +x bazel-*.sh && \
  ./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \
  cd / && \
  rm -f /bazel/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh

WORKDIR /usr/local
RUN git clone --recursive https://github.com/deepmind/sonnet

RUN ln -s /usr/lib/x86_64-linux-gnu/libcudnn.so /usr/local/cuda/lib64/libcudnn.so
RUN ln -s /usr/lib/x86_64-linux-gnu/libcudnn.so.5 /usr/local/cuda/lib64/libcudnn.so.5

WORKDIR /usr/local/sonnet/tensorflow
ENV CC_OPT_FLAGS=-march=native PYTHON_BIN_PATH=/usr/bin/python PYTHON_LIB_PATH=/usr/local/lib/python2.7/dist-packages TF_NEED_MKL=0 TF_NEED_JEMALLOC=1 TF_NEED_GCP=0 TF_NEED_HDFS=0 TF_ENABLE_XLA=0 TF_NEED_VERBS=0 TF_NEED_OPENCL=0 TF_NEED_CUDA=1 TF_CUDA_CLANG=0 TF_CUDA_VERSION=8.0 CUDA_TOOLKIT_PATH=/usr/local/cuda GCC_HOST_COMPILER_PATH=/usr/bin/gcc TF_CUDNN_VERSION=5.1.10 CUDNN_INSTALL_PATH=/usr/local/cuda

RUN ./configure

WORKDIR /usr/local/sonnet
RUN mkdir /tmp/sonnet && bazel build --config=opt --copt="-D_GLIBCXX_USE_CXX11_ABI=0" :install && ./bazel-bin/install /tmp/sonnet && pip install /tmp/sonnet/*.whl

RUN mkdir /workspace
WORKDIR /workspace
RUN ["/bin/bash"]
