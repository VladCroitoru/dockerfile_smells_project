FROM mottosso/mayabase-ubuntu

MAINTAINER marcus@abstractfactory.io

# Download and unpack distribution first, Docker's caching
# mechanism will ensure that this only happens once.
RUN wget http://download.autodesk.com/us/support/files/maya_2015_service_pack_5/Autodesk_Maya_2015_SP5_English_Linux.tgz -O maya.tgz && \
    mkdir /maya && tar -xvf maya.tgz -C /maya && \
    rm maya.tgz

WORKDIR /maya

# Convert RPC package to Debian package
# This an take a long time ~15 to 30 mins
RUN for i in *.rpm; do \
  sudo alien -cv $i; \
done

# Install Maya
RUN dpkg -i *.deb && \
    cp lib* /usr/lib/ && \
    mkdir /usr/tmp && \
    chmod 777 /usr/tmp

# Create symlinks
RUN ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.0.9.8 /usr/autodesk/maya2015-x64/lib/libcrypto.so.10 && \
    ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.0.9.8 /usr/autodesk/maya2015-x64/lib/libcrypto.so.0.9.8

# Setup environment
ENV MAYA_LOCATION=/usr/autodesk/maya2015-x64/
ENV PATH=$MAYA_LOCATION/bin:$PATH

# Cleanup
WORKDIR /root
RUN rm -r /maya
