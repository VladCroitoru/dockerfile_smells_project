FROM ubuntu:latest

USER root
# RUN conda update conda 
RUN apt update

RUN apt-get update  -y -q
RUN apt-get install -q -y sssd libnss-sss libpam-sss
RUN apt install -q -y build-essential libssl-dev libffi-dev python3-dev
RUN apt install -q -y python3-pip
RUN pip3 install vos cadcdata cadctap cadcutils
RUN apt install -q -y python3-numpy
RUN apt install -q -y python3-scipy

# system settings and permissions
ADD nsswitch.conf /etc/
ADD nofiles.conf /etc/security/limits.d/
RUN touch /etc/sudo.conf && echo "Set disable_coredump false" > /etc/sudo.conf
# generate missing dbus uuid (issue #47)
RUN dbus-uuidgen --ensure


## see https://bugzilla.redhat.com/show_bug.cgi?id=1773148
RUN apt install  -q -y iraf
RUN apt install  -q -y xterm 
RUN apt install -q -y git
RUN apt-get install -y libx11-dev
RUN apt-get install -y iraf-dev
RUN pip3 install astropy
RUN pip3 install ccdproc
RUN pip3 install ephem
RUN pip3 install mp_ephem

## install xpa
WORKDIR /opt/
RUN git clone https://github.com/ericmandel/xpa.git
WORKDIR xpa
# We configure the files for a shared library.
RUN ./configure --enable-shared=yes
# I needed to install make, but others may have it already.
RUN make install
# Now we move the libraries we just made into the appropriate location in the OS.
RUN mv libxpa* /usr/lib
# Rebuild any static references in the library that would have been broken by the move.
WORKDIR /usr/lib
RUN ranlib libxpa.a

RUN pip3 install pyraf
RUN apt install -q -y libxt-dev
RUN pip3 install pyds9

RUN pip3 install jupyterlab

ARG BUILDDIR=/opt/findMoving
RUN mkdir -p ${BUILDDIR}
WORKDIR ${BUILDDIR}
COPY src  ./
RUN python3 -m pip install -r requirements.txt
RUN python3 setup.py install 
RUN apt install -q -y cfitsio

RUN mkdir /skaha
ADD init.sh /skaha/

CMD [ "bash" ]

