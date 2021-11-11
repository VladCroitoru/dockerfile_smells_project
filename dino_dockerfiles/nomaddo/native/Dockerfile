FROM debian:stretch

# add unstable repositoty to install clang-format-7.0
# NOTE: the content of unstable repo will be changed
RUN echo -n 'deb http://ftp.debian.org/debian unstable main contrib non-free' >> /etc/apt/sources.list

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
   git curl cmake bc automake libtool build-essential pkg-config make debian-archive-keyring \
   ca-certificates devscripts python unzip libllvm3.9 llvm-3.9-dev opencl-c-headers \
   g++-6 clang-3.9 ocl-icd-opencl-dev ocl-icd-dev clang-format-7 diffutils \
   wget \
 && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# add clang-format
RUN update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-7 11
