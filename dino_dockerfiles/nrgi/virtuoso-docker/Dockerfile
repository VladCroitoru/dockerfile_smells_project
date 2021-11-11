FROM ubuntu:14.04

# Install the Virtuoso dependencies
# see the README at https://github.com/openlink/virtuoso-opensource
RUN apt-get update
RUN apt-get install -y gcc autoconf automake libtool flex bison gperf gawk m4 make libssl-dev libreadline-dev git
RUN apt-get clean

# Fetch a copy of Virtuoso from GitHub
WORKDIR /usr/local/src
RUN git clone https://github.com/openlink/virtuoso-opensource.git && cd virtuoso-opensource && git checkout 39e64c3a7ad8dd2143e5bb5d9ee81019e20c25bf
# We checkout the commit explicitly by ID so we have better control over
# exactly what code we're running
#RUN git checkout stable/7

# We use the stable branch for verison 7
WORKDIR /usr/local/src/virtuoso-opensource

# We follow the installation instructions in the Virtuoso README
# see the README at https://github.com/openlink/virtuoso-opensource
RUN ./autogen.sh
# from the README - additonal flags for Linux 64-bit
RUN CFLAGS="-O2 -m64"
RUN export CFLAGS
# We compile with libreadline as we may want to use this with OntoWiki
# See 'Debian/Ubuntu Tip' https://github.com/AKSW/OntoWiki/wiki/VirtuosoBackend
RUN ./configure --prefix=/usr/local/ --with-readline=/usr/lib/libreadline.so
RUN make
RUN make install

# Make it available at http://localhost:8890
EXPOSE 8890

#Fire it up
# See 'Getting Started' in the README
WORKDIR /usr/local/var/lib/virtuoso/db/
CMD virtuoso-t -df
