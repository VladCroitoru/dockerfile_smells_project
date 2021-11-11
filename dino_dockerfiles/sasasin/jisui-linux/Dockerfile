FROM ubuntu:16.04

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get autoremove
RUN apt-get autoclean
RUN apt-get install -y git-core
RUN apt-get install -y bash-completion
RUN apt-get install -y apt-utils
RUN apt-get install -y libjpeg-turbo-progs
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN apt-get install -y imagemagick
RUN apt-get install -y libimage-size-perl
RUN apt-get install -y libmoose-perl
RUN apt-get install -y libpdf-create-perl
RUN apt-get install -y optipng
RUN apt-get install -y pdftk
RUN apt-get install -y pngnq
RUN apt-get install -y poppler-data
RUN apt-get install -y openjdk-8-jdk maven
RUN apt-get install -y unzip

ENV PATH=/root/script:$PATH

CMD ["/bin/bash"]
