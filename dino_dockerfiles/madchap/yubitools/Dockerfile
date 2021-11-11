FROM ubuntu:xenial

# change this to the name of the user you're using on your dekstop, to get X back through the socket
#ENV IMAGEUSER fblaise
#ENV IMAGEUSERUID 1000

USER root

# build deps
# RUN apt-get update \
#   && apt-get -y install \
# 	debhelper \
# 	python3-pip \
# 	swig \
# 	python \
# 	libpcsclite-dev \
# 	libssl-dev \
# 	libffi-dev \
# 	qtbase5-dev \
# 	qtdeclarative5-dev \
# 	qml-module-qtquick-controls \
# 	qml-module-qtquick-dialogs \
# 	qml-module-io-thp-pyotherside \
# 	qml-module-qt-labs-settings \
# 	libqt5svg5-dev 

RUN apt-get update
# add missing packages to have apt-add-repository
RUN apt-get -y install software-properties-common python-software-properties

# install yubikey-tools
RUN apt-add-repository ppa:yubico/stable
RUN apt-get update \
  && apt-get install -y yubikey-manager-qt yubikey-manager yubioath-desktop \
  && apt-get install -y yubikey-personalization-gui yubico-piv-tool yubikey-piv-manager yubikey-personalization \
  && apt-get install -y man

# get yubioath          
#RUN wget https://${IMAGEUSER}s.yubico.com/yubioath-desktop/Releases/yubioath-desktop-${YUBIOATH_VERSION}.tar.gz \
#  && wget https://${IMAGEUSER}s.yubico.com/yubioath-desktop/Releases/yubioath-desktop-${YUBIOATH_VERSION}.tar.gz.sig

# import the key from the sig..
#RUN gpg --recv `gpg yubioath-desktop-${YUBIOATH_VERSION}.tar.gz.sig 2>&1 |awk '/RSA key/ {print $14}'`

# build yubioath
#RUN gpg --verify yubioath-desktop-${YUBIOATH_VERSION}.tar.gz.sig \
#  && tar xf yubioath-desktop-${YUBIOATH_VERSION}.tar.gz \
#  && cd yubioath-desktop-${YUBIOATH_VERSION} \
#  && qmake -qt=qt5 && make

# run deps
#RUN apt-get -y install \
#	python3-yubikey-manager \
#	qml-module-io-thp-pyotherside \
#	qml-module-qtquick-controls \
#	qml-module-qtquick-dialogs \
#	qml-module-qt-labs-settings \
#	pcscd

RUN rm -rf /var/lib/apt/lists/*

#RUN adduser --gecos ${IMAGEUSER} --uid ${IMAGEUSERUID} --disabled-password ${IMAGEUSER}
#RUN usermod -aG sudo ${IMAGEUSER}
#RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY docker-entrypoint.sh /

#USER ${IMAGEUSER}
#ENV HOME /home/${IMAGEUSER}

ENTRYPOINT ["/docker-entrypoint.sh"]
