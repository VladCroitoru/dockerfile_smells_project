FROM ubuntu:latest

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

WORKDIR /opt/electrum

RUN apt-get update \
	&& apt-get install -y git python-pip python-slowaes python-socksipy pyqt4-dev-tools \
	&& pip install pyasn1 pyasn1-modules pbkdf2 tlslite qrcode mnemonic ecdsa protobuf \
	&& pip install https://github.com/trezor/python-mnemonic/archive/d8328653f8247ee6b080870845e8efaadcd4984e.zip \
	&& git clone -b greenaddress-2of3-recovery --single-branch https://github.com/greenaddress/electrum.git . \
	&& pyrcc4 icons.qrc -o gui/qt/icons_rc.py 

# assuming same uid+gid as Docker host's X server owner
# otherwise use `-v /tmp:/tmp --ipc=host --pid=host` per http://stackoverflow.com/a/29658804
RUN useradd -m electrum

USER electrum

ENV HOME /home/electrum
ENV QT_X11_NO_MITSHM 1

CMD ["/opt/electrum/electrum"]
