# Sets up basic toolchain required for Gitlab builds
FROM ubuntu:latest

# configure timezone for build-essential
ENV TZ=America
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -y update && \
    apt-get -y install \
        build-essential \
        cmake cpputest \
        pkg-config \ 
        cppcheck \
        clang-tidy