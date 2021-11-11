FROM project8/cvmfs-dependencies-katydid:build-2018-04-23

RUN mkdir -p /tmp_install

ADD ./setup.sh /tmp_install/setup.sh
ADD ./download_pkg.sh /tmp_install/download_pkg.sh
ADD ./install.sh /tmp_install/install.sh
ADD ./run-cvmfs-install.sh /tmp_install/run-cvmfs-install.sh
ADD ./cleanup.sh /tmp_install/cleanup.sh

# sleep for 1s added to avoid weird "text file busy" error when building on docker hub
RUN cd /tmp_install && \
    ls && \
    source /opt/rh/devtoolset-3/enable && \
    rm /usr/lib64/libhdf5* && \
    /tmp_install/run-cvmfs-install.sh && \
    /tmp_install/cleanup.sh && \
    rm -rf /tmp_install
