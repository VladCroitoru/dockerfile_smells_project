FROM ubuntu:zesty
RUN apt-get update && apt-get install -y software-properties-common python-software-properties
RUN apt-get install -y curl
RUN apt-get install -y python3-pip
RUN pip3 install cpplint
RUN pip3 install pyyaml
RUN apt-get install -y git flex bison cmake
RUN cd opt && git clone https://github.com/doxygen/doxygen.git && cd doxygen && mkdir build; cd build && cmake -G "Unix Makefiles" .. && make -j && make install
RUN apt-get install -y default-jdk
RUN pip3 install openpyxl
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt-add-repository -yu 'deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu xenial main'
RUN add-apt-repository --remove ppa:ubuntu-toolchain-r/test
RUN apt-get update
RUN apt-get install -y gcc-7 g++-7
RUN pip3 install gcovr
# Patch gcovr
RUN perl  -p -i -e 's|itertools.izip|zip|g' /usr/local/bin/gcovr