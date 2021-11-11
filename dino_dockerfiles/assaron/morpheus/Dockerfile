FROM ubuntu:14.04

RUN apt-get -y update
RUN apt-get -y dist-upgrade
RUN apt-get install -y software-properties-common
RUN apt-get -y install git
RUN apt-get -y install libcairo2-dev
RUN apt-get -y install libxt-dev
RUN apt-get -y install libssl-dev
RUN apt-get -y install libssh2-1-dev
RUN apt-get -y install libcurl4-openssl-dev

RUN apt-get -y install apache2
RUN touch /etc/apache2/sites-available/opencpu2.conf
RUN printf "ProxyPass /ocpu/ http://localhost:8001/ocpu/\nProxyPassReverse /ocpu/ http://localhost:8001/ocpu\n" >> /etc/apache2/sites-available/opencpu2.conf
RUN a2ensite opencpu2

RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list'
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
RUN gpg -a --export E084DAB9 | sudo apt-key add -
RUN apt-get update
RUN apt-get -y install r-base

RUN R -e 'source("https://bioconductor.org/biocLite.R"); biocLite("Biobase"); install.packages("devtools", repo = "http://cran.gis-lab.info"); library(devtools); install_github("hadley/scales"); install_github("baba-beda/morpheusR")'
RUN cd /var/www/html && \
    git clone https://github.com/baba-beda/morpheus.js.git morpheus && \
    cd
    
RUN add-apt-repository -y ppa:opencpu/opencpu-1.6 && \
  apt-get update && \
  apt-get install -y opencpu-lib

RUN a2enmod proxy_http

EXPOSE 80
EXPOSE 443
EXPOSE 8004

CMD service apache2 start && R -e 'opencpu::opencpu$start(8001)' && tail -F /var/log/opencpu/apache_access.log
