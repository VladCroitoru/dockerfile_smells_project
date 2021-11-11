FROM ubuntu:16.04
RUN apt-get update --quiet \
    && apt-get install --quiet --yes curl git
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" \
    | tee /etc/apt/sources.list.d/bazel.list \
    && curl https://bazel.build/bazel-release.pub.gpg | apt-key add - \
    && apt-get update --quiet
# Bazel 0.5.3
RUN apt-get install --quiet --yes bazel
