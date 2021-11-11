FROM openmicroscopy/ome-files-cpp-u1604:latest
MAINTAINER ome-devel@lists.openmicroscopy.org.uk

# Install JDK7 and Maven
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk
RUN apt-get -y install maven


# Build OME Files performance component
COPY . /git/ome-files-performance

WORKDIR /build-ome-files
RUN cmake -DCMAKE_INSTALL_PREFIX:PATH=/install \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_PREFIX_PATH="$OME_FILES_BUNDLE" \
  -DCMAKE_PROGRAM_PATH=$OME_FILES_BUNDLE/bin \
  -DCMAKE_LIBRARY_PATH=$OME_FILES_BUNDLE/lib \
  /git/ome-files-performance
RUN cmake --build .
RUN cmake --build . --target install

# Build Bio-Formats performance component
WORKDIR /git/ome-files-performance
RUN mvn clean install

# Set locale to UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

ENTRYPOINT ["/bin/bash", "/git/ome-files-performance/scripts/run_benchmarking"]
