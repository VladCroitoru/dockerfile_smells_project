FROM jangrewe/gitlab-ci-android:latest
LABEL maintainer="Oliver Spryn"

RUN mkdir -p /build
RUN curl --location --output /build/ktlint https://github.com/pinterest/ktlint/releases/latest/download/ktlint
RUN chmod +x /build/ktlint

ENV PATH "$PATH:/build"
