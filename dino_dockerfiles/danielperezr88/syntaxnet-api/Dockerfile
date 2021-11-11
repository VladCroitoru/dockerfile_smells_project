FROM ubuntu:17.10

MAINTAINER danielperezr88 <danielperezr88@gmail.com>

RUN apt-get update && apt-get install -y \
        build-essential \
        curl \
        g++ \
        git \
        libfreetype6-dev \
        libpng-dev \
        libzmq3-dev \
        openjdk-8-jdk

RUN apt-get update && apt-get install -y \
        pkg-config \
        python-dev \
        python-numpy \
        python-pip \
        software-properties-common \
        swig \
        unzip \
        zip

RUN apt-get update && apt-get install -y \
        zlib1g-dev \
		libcurl3-dev \
		wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN update-ca-certificates -f

# Set up Bazel.

# Running bazel inside a `docker build` command causes trouble, cf:
#   https://github.com/bazelbuild/bazel/issues/134
# The easiest solution is to set up a bazelrc file forcing --batch.
RUN echo "startup --batch" >>/root/.bazelrc
# Similarly, we need to workaround sandboxing issues:
#   https://github.com/bazelbuild/bazel/issues/418
RUN echo "build --spawn_strategy=standalone --genrule_strategy=standalone" \
    >>/root/.bazelrc
ENV BAZELRC /root/.bazelrc
# Install the most recent bazel release.
ENV BAZEL_VERSION 0.5.4
WORKDIR /
RUN mkdir /bazel && \
    cd /bazel && \
    curl -fSsL -O https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \
    curl -fSsL -o /bazel/LICENSE.txt https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE.txt && \
    chmod +x bazel-*.sh && \
    ./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \
    cd / && \
    rm -f /bazel/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh


# Syntaxnet dependencies

RUN pip install -U protobuf==3.0.0b2
RUN pip install asciitree
RUN git clone --recursive https://github.com/danielperezr88/syntaxnet-api.git \
    && cd /syntaxnet-api/tensorflow-models \
    && git checkout dee751fafb66e511c6fec02b572670b50bc517fa \
    && cd /syntaxnet-api \
    && git submodule update --init --recursive

RUN cd /syntaxnet-api/tensorflow-models/syntaxnet/tensorflow \
	&& curl -fSL "https://github.com/bazelbuild/bazel/files/716847/diff.patch.txt" -o /syntaxnet-api/tensorflow-models/syntaxnet/tensorflow/diff.patch.txt \
	&& patch -p1 < diff.patch.txt

RUN cd /syntaxnet-api/tensorflow-models/syntaxnet/syntaxnet \
	&& curl -fSL "https://gist.githubusercontent.com/danielperezr88/044e757f340218a0f445693d15ff25b2/raw/24c55b040fb50149b237a31c19c4c114c56c4cf6/parser_trainer_test_patch.txt" \
		-o /syntaxnet-api/tensorflow-models/syntaxnet/syntaxnet/parser_trainer_test_patch.txt \
	&& patch -p1 < parser_trainer_test_patch.txt

RUN cd /syntaxnet-api/tensorflow-models/syntaxnet/tensorflow \
	&& echo "\ny\n\n\n\n" | ./configure

RUN cd /syntaxnet-api/tensorflow-models/syntaxnet/tensorflow/tensorflow \
	&& curl -fSL "https://gist.githubusercontent.com/danielperezr88/49b1ea867f026aa2c6541b3daced4a3a/raw/fc5abe227a05d23e92ceda4288092814f343bc0f/syntaxnetapi-workspacebzl-patch.txt" \
		-o /syntaxnet-api/tensorflow-models/syntaxnet/tensorflow/tensorflow/syntaxnetapi-workspacebzl-patch.txt \
	&& patch -p1 < syntaxnetapi-workspacebzl-patch.txt

RUN cd /syntaxnet-api/tensorflow-models/syntaxnet \
	&& bazel test syntaxnet/... util/utf8/...

RUN mkdir /syntaxnet-api/tensorflow-models/syntaxnet/universal_models \
    && cd /syntaxnet-api/tensorflow-models/syntaxnet/universal_models \
	&& for LANG in Ancient_Greek-PROIEL Basque Bulgarian Chinese Croatian Czech Danish Dutch English Estonian Finnish French Galician \
		German Greek Hebrew Hindi Hungarian Indonesian Italian Latin-PROIEL Norwegian Persian Polish Portuguese Slovenian Spanish Swedish; \
		do wget http://download.tensorflow.org/models/parsey_universal/${LANG}.zip; unzip ${LANG}.zip; rm ${LANG}.zip; done

RUN apt-get update && apt-get -y install python3-pip

RUN cd /syntaxnet-api && pip3 install -r requirements.txt

EXPOSE 7000

WORKDIR /syntaxnet-api/

CMD python3 flask_server.py
