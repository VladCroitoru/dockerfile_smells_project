FROM phusion/passenger-ruby22

# install postgres
ADD config/postgresql.list /etc/apt/sources.list.d/postgresql.list
RUN sudo apt-get update
RUN sudo apt-get install wget -y
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
RUN sudo apt-get update
RUN sudo apt-get install postgresql-client-9.5 -y

# install imagemagick
WORKDIR /tmp
ADD lib/ImageMagick-6.9.3-0.tar.gz /tmp/ImageMagick-6.9.3-0.tar.gz
WORKDIR /tmp/ImageMagick-6.9.3-0.tar.gz/ImageMagick-6.9.3-0
RUN chmod +x configure
RUN ./configure
RUN make
RUN sudo make install
RUN sudo ldconfig /usr/local/lib

# install node-v5.4.1
RUN sudo apt-get install make g++ libssl-dev git -y
WORKDIR /tmp
ADD lib/node-v5.4.1.tar.gz /tmp/node-v5.4.1.tar.gz
WORKDIR /tmp/node-v5.4.1.tar.gz/node-v5.4.1
RUN chmod +x configure
RUN ./configure
RUN make
RUN sudo make install

# install stunserver
RUN sudo apt-get update
RUN sudo apt-get install libboost-dev -y
ADD lib/stunserver-1.2.9.tgz /home/app/stunserver-1.2.9.tgz
WORKDIR /home/app/stunserver-1.2.9.tgz/stunserver
RUN make
RUN sudo cp stunserver /usr/sbin/stunserver
ADD config/stuntman-server/stuntman-server /etc/init.d/stuntman-server
RUN sudo chmod +x /etc/init.d/stuntman-server
RUN sudo service stuntman-server start

# Install signalmaster:
WORKDIR /home/app
RUN git clone https://github.com/andyet/signalmaster.git
ADD config/signalmaster/package.json /home/app/signalmaster/package.json
WORKDIR /home/app/signalmaster
RUN npm install
RUN npm install

# install pdfinfo
RUN sudo apt-get install poppler-utils -y
RUN sudo apt-get install redis-tools -y
