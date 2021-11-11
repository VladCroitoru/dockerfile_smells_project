FROM r-base:latest
MAINTAINER quanteek

RUN useradd -ms /bin/bash -G staff user01
USER user01
WORKDIR /home/user01
COPY install_packages.R /home/user01/
RUN Rscript install_packages.R
COPY sis.R /home/user01/
COPY data.txt /home/user01/
COPY run.sh /home/user01/

