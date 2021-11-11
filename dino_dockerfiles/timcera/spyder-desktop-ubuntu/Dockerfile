FROM ubuntu:xenial
MAINTAINER Tim Cera <tim@cerazone.net>

RUN    apt-get -y update
RUN    apt-get -y install python3-numpy \
                          python3-scipy \
                          python3-matplotlib \
                          ipython3 \
                          ipython3-notebook \
                          python3-pandas \
                          python3-sympy \
                          python3-nose
RUN    apt-get -y install libjs-jquery \
                          libjs-mathjax \
                          python3-pyqt4 \
                          tortoisehg \
                          gitk \
                          ipython3-qtconsole \
                          python3-pep8 \
                          pyflakes \
                          pylint \
                          python3-jedi \
                          python3-psutil \
                          python3-sphinx
RUN    apt-get -y install python3-pip
RUN    pip3 install rope_py3k
RUN    pip3 install spyder
RUN    apt-get -y install gfortran
RUN    pip3 install wdmtoolbox
RUN    pip3 install hspfbintoolbox
RUN    pip3 install swmmtoolbox
RUN    pip3 install flopy

RUN    apt-get clean \
    && apt-get purge

## cleanup of files from setup
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Called when the Docker image is started in the container
ADD start.sh /start.sh
RUN chmod 0755 /start.sh

CMD /start.sh

