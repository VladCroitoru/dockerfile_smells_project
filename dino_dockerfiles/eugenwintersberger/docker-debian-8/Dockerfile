FROM debian:8

COPY debian-backports.list /etc/apt/sources.list.d
RUN apt-get -y update
RUN apt-get -y install ninja-build python-setuptools g++ doxygen git libboost-all-dev
RUN apt-get -y -t jessie-backports install cmake
RUN apt-get -y gfortran
RUN apt-get clean


RUN easy_install pip
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