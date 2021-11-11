FROM ubuntu

COPY . /src

RUN apt-get update
RUN apt-get install -y make gcc libc6-dev  gettext
                            #   ^ ctypes.h ^ xgettext

RUN cd /src && make
