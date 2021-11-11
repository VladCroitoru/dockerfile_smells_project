FROM maci0/systemd
MAINTAINER "Sean McCully <sean_mccully@yahoo.com>"
RUN yum update -y
RUN yum groups mark convert
RUN yum group install -y "Development Tools"
#RUN yum group install -y "C Development Tools and Libraries"
RUN yum install -y sudo vim git openssh-server openssh-clients openssl openssl-devel boost-devel dh-autoreconf ccache pkgconfig libdb libdb-devel libdb-cxx libdb-cxx-devel protobuf protobuf-devel

#add bitcoin user with passwd: bitcoind
RUN useradd -mc "Bit₵oin U$er" bitcoin -p abioytFqlXVrA
#allow passwordless sudo for convience
RUN echo 'bitcoin ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN git clone -b 0.9 git://github.com/bitcoin/bitcoin.git /home/bitcoin/bitcoin
RUN git clone -b OpenSSL_1_0_2-stable https://github.com/openssl/openssl.git /home/bitcoin/openssl

RUN cd /home/bitcoin/openssl && ./config --prefix=/usr shared enable-ec enable-ecdh enable-ecdsa
RUN cd /home/bitcoin/openssl && make
RUN cd /home/bitcoin/openssl && make install

#need to fix BerkeleyDB to get rid of the 1st flag
RUN /bin/bash /home/bitcoin/bitcoin/autogen.sh
RUN cd /home/bitcoin/bitcoin && ./configure --with-incompatible-bdb --without-qt
RUN cd /home/bitcoin/bitcoin && make
RUN cd /home/bitcoin/bitcoin && make install

RUN mkdir -p /opt/bitcoin
COPY bitcoin.conf /opt/bitcoin/bitcoin.conf
COPY bitcoin.service /etc/systemd/system/bitcoind.service
#Modify bitcoin.conf
RUN P=`openssl rand -hex 8`;sed s/RPC_USER/$P/g /opt/bitcoin/bitcoin.conf > /opt/bitcoin/bitcoin.conf.TMP && mv -f /opt/bitcoin/bitcoin.conf.TMP /opt/bitcoin/bitcoin.conf
RUN echo `openssl rand -base64 128` > pass; sed -e 's/[\/&]/\\&/g' pass > pass.TMP;P=`cat pass.TMP`;sed s/RPC_PASSWORD/"$P"/g /opt/bitcoin/bitcoin.conf > /opt/bitcoin/bitcoin.conf.TMP && mv -f /opt/bitcoin/bitcoin.conf.TMP /opt/bitcoin/bitcoin.conf;rm -rf pass pass.TMP
RUN /usr/bin/openssl req -newkey rsa:4096 -nodes -keyout /opt/bitcoin/server.pem  -x509 -days 3000  -out /opt/bitcoin/server.cert -subj "/C=US/ST=/L=/O=/CN=localhost"

#we've build the binary, now copy it so we can execute anywhere in the container
RUN chown -R bitcoin:bitcoin /home/bitcoin
RUN chown -R bitcoin:bitcoin /opt/bitcoin
RUN systemctl enable bitcoind
RUN systemctl enable sshd

CMD /usr/lib/systemd/systemd
