FROM ubuntu:20.04

RUN echo "Updating Ubuntu"
RUN apt-get update && apt-get upgrade -y

RUN echo "Installing dependencies..."
RUN apt install -y \
			ccache \
			clang \
			clang-format \
			clang-tidy \
			cppcheck \
			curl \
			doxygen \
			gcc \
			git \
			graphviz \
			make \
			ninja-build \
			python3 \
			python3-pip \
			tar \
			unzip \
			vim \
			meson

RUN echo "Installing dependencies not found in the package repos..."
RUN pip3 install conan