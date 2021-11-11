FROM ghcr.io/derlih/aosp-build-docker:main

ARG AOSP_TAG

WORKDIR /aosp-src
RUN --mount=type=secret,id=GIT_CONFIG,target=/root/.gitconfig \
    repo init -u https://android.googlesource.com/platform/manifest -b $AOSP_TAG -g all,-notdefault,tools && \
    repo sync -c --no-clone-bundle -j20
