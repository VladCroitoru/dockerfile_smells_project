FROM rocker/shiny

MAINTAINER iiichtang

RUN apt-get install -y gdebi-core && \
    Rscript -e "install.packages('RJSONIO')" && \
    Rscript -e "install.packages('ggplot2')"

RUN wget https://download2.rstudio.org/rstudio-server-0.99.473-amd64.deb && \
    gdebi --non-interactive rstudio-server-0.99.473-amd64.deb && \
    rm -f rstudio-server-0.99.473-amd64.deb

RUN useradd -d /home/rstudio -s /bin/bash -p $(echo rstudio | openssl passwd -1 -stdin) rstudio && \ 
    mkdir /home/rstudio && \
    chown -R rstudio /home/rstudio && \
    chgrp -R rstudio /home/rstudio && \
    usermod -a -G staff rstudio

EXPOSE 8787

CMD rstudio-server start && sh /usr/bin/shiny-server.sh
