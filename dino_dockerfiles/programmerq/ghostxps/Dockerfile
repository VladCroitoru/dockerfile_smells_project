#USAGE: cat file.xps | docker run -i ghostxps > file.pdf
FROM debian:jessie
MAINTAINER Jeff Anderson <jeff@docker.com>

RUN apt-get -y update
RUN apt-get -y install libxt-dev libxext-dev

#ADD ghostxps-9.15-linux-x86_64.tar.gz /source/
ADD http://downloads.ghostscript.com/public/binaries/ghostxps-9.15-linux-x86_64.tgz /source/
ADD http://downloads.ghostscript.com/public/ghostpdl-9.15.tar.gz /source/
RUN cd /source && tar xavf ghostxps-9.15-linux-x86_64.tgz

CMD /source/ghostxps-9.15-linux-x86_64/gxps-915-linux_x86_64 -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -sOutputFile=- -
