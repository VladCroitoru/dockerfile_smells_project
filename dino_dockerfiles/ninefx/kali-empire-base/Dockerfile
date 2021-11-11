FROM kalilinux/kali-linux-docker

RUN apt-get -y update && apt-get -y dist-upgrade
RUN apt-get install -y make g++ python-dev python-m2crypto swig python-pip libxml2-dev default-jdk libssl-dev wget curl sudo git lsb-release
RUN pip install --upgrade urllib3 setuptools pycrypto iptools pydispatcher flask macholib dropbox pyopenssl pyinstaller zlib_wrapper netifaces
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-3_amd64.deb
RUN wget http://ftp.debian.org/debian/pool/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb
RUN dpkg -i libicu52_52.1-3_amd64.deb
RUN dpkg -i libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb
RUN rm libicu52_52.1-3_amd64.deb libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/14.04/prod.list | tee /etc/apt/sources.list.d/microsoft.list
RUN apt-get -y update
RUN apt-get install -y powershell

CMD ["/bin/bash"]
