FROM tensorflow/tensorflow:latest-devel-py3

ENV DEBIAN_FRONTEND noninteractive
RUN mkdir -p /usr/src/app && apt-get update && apt-get --install-suggests --yes dist-upgrade && apt-cache pkgnames python3 | egrep -i "^python3-(numpy|pyfftw|soundfile|theano|keras|youtube.dl|matplotlib)$" | xargs apt-get --yes install \
    libfftw3-dev \
    liblapack-dev \
    youtube-dl

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --compile --process-dependency-links -r requirements.txt --upgrade

WORKDIR /tensorflow

ONBUILD RUN CFLAGS="-march=native" tensorflow/tools/ci_build/builds/configured CPU \
    bazel build --copt="-march=native" -c opt tensorflow/tools/pip_package:build_pip_package && \
    bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/pip && \
    pip3 --no-cache-dir install --force-reinstall --compile --upgrade /tmp/pip/tensorflow-*.whl && \
    rm -rf /tmp/pip && \
    rm -rf /root/.cache

ONBUILD WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD COPY . /usr/src/app

ONBUILD RUN CFLAGS="-march=native" pip3 install --compile --process-dependency-links -r requirements.txt --upgrade
