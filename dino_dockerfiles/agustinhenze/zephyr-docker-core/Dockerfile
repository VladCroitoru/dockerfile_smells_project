FROM debian:stretch-backports

RUN apt-get update && apt-get install eatmydata -y && rm -rf /var/lib/apt

RUN apt-get update && eatmydata apt-get install make gcc libc6-dev libncurses5-dev clang-3.9 lldb-3.9 sudo \
    python3-yaml python3-ply python3-pip python3-setuptools python3-wheel ccache doxygen device-tree-compiler git \
    python3-pyelftools wget xz-utils gperf bash-completion \
    --no-install-recommends -y && rm -rf /var/lib/apt

RUN apt-get update && eatmydata apt-get install cmake cmake-curses-gui -t stretch-backports \
    --no-install-recommends -y && rm -rf /var/lib/apt

RUN pip3 install awscli breathe==4.6.0 sphinx==1.5.5 sphinx_rtd_theme junit2html \
    git+https://github.com/zephyriot/gitlint.git pykwalify

ENV ZEPHYR_SDK_VERSION 0.9.2

RUN wget --quiet https://github.com/zephyrproject-rtos/meta-zephyr-sdk/releases/download/${ZEPHYR_SDK_VERSION}/zephyr-sdk-${ZEPHYR_SDK_VERSION}-setup.run \
 && chmod +x zephyr-sdk-${ZEPHYR_SDK_VERSION}-setup.run \
 && ./zephyr-sdk-${ZEPHYR_SDK_VERSION}-setup.run --quiet -- -d /opt/sdk/zephyr-sdk-${ZEPHYR_SDK_VERSION} \
 && rm zephyr-sdk-${ZEPHYR_SDK_VERSION}-setup.run
