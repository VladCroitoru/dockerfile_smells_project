FROM alpine
RUN apk --update add gnutls gnutls-dev libmicrohttpd libmicrohttpd-dev gcc git make g++ linux-headers libusb libusb-dev eudev eudev-dev coreutils && \
    cd /root && \
    git clone https://github.com/colinodell/open-zwave && \
    cd open-zwave && \
    git checkout V1.5-with-customizations && \
    make && \

    cd .. && \
    git clone https://github.com/colinodell/open-zwave-control-panel.git && \
    cd open-zwave-control-panel && \
    sed -i 's/#GNUTLS := -lgnutls/GNUTLS := -lgnutls/' Makefile && \
    sed -i 's/#LIBUSB := -ludev/LIBUSB := -ludev/' Makefile && \
    sed -i 's/#LIBS := $(LIBZWAVE) $(GNUTLS) $(LIBMICROHTTPD) -pthread $(LIBUSB) -lresolv/LIBS := $(LIBZWAVE) $(GNUTLS) $(LIBMICROHTTPD) -pthread $(LIBUSB) -lresolv/' Makefile && \
    sed -i 's/LIBUSB := -framework IOKit -framework CoreFoundation/#LIBUSB := -framework IOKit -framework CoreFoundation/' Makefile && \
    sed -i 's/LIBS := $(LIBZWAVE) $(GNUTLS) $(LIBMICROHTTPD) -pthread $(LIBUSB) $(ARCH) -lresolv/#LIBS := $(LIBZWAVE) $(GNUTLS) $(LIBMICROHTTPD) -pthread $(LIBUSB) $(ARCH) -lresolv/' Makefile && \
    make && \
    ln -sd ../open-zwave/config && \
    apk del libmicrohttpd-dev gcc git make g++ linux-headers libusb-dev eudev-dev coreutils

EXPOSE 8090
WORKDIR /root/open-zwave-control-panel/
ENTRYPOINT ["/root/open-zwave-control-panel/ozwcp"]
