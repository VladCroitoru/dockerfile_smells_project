FROM ubuntu:17.10

RUN apt-get -y update
RUN apt-get -y install cmake ninja-build python-pip
RUN apt-get -y install g++ doxygen
RUN apt-get -y install git
RUN apt-get -y install libboost-all-dev
RUN apt-get clean

RUN pip install conan
RUN pip install gitpython
RUN conan remote remove conan-center
RUN conan remote remove conan-transit
RUN conan remote add desypackages https://api.bintray.com/conan/eugenwintersberger/desy-packages
RUN conan remote add conan-community https://api.bintray.com/conan/conan-community/conan
RUN conan remote add conan-center https://conan.bintray.com
RUN conan remote add conan-transit https://conan-transit.bintray.com
RUN conan user
RUN mkdir /src

WORKDIR /src
