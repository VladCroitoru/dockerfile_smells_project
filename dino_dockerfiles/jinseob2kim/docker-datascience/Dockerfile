FROM ubuntu:18.04

MAINTAINER Jinseob Kim "jinseob2kim@gmail.com"

# Setup apt to be happy with no console input
ENV DEBIAN_FRONTEND noninteractive

# Install dependencies and Download 

RUN apt-get update && apt-get install -y \
    udev \
    locales \
    software-properties-common \
    file \
    curl \
    git \
    sudo \
    wget \
    gdebi-core \
    vim \
    r-base \
    psmisc \
    python3 \
    python3-pip \
    npm \
    nodejs \
    supervisor \
    nginx && \
    npm install -g configurable-http-proxy && \
    pip3 install jupyterhub && \
    pip3 install --upgrade notebook && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Prevent bugging us later about timezones
RUN ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

# Use UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8


# Add user (js)
RUN adduser js --gecos 'First Last,RoomNumber,WorkPhone,HomePhone' --disabled-password && \
    sh -c 'echo js:js | sudo chpasswd' && \
    usermod -aG sudo js


# Update R -latest version
#RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu bionic/" | sudo tee -a /etc/apt/sources.list && \
#    gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \
#    gpg -a --export E084DAB9 | sudo apt-key add - && \
#    apt-get update && \
#    apt-get install r-base r-base-dev

# Install Rstudio-server
ARG RSTUDIO_VERSION

RUN RSTUDIO_LATEST=$(wget --no-check-certificate -qO- https://s3.amazonaws.com/rstudio-server/current.ver) && \ 
    [ -z "$RSTUDIO_VERSION" ] && RSTUDIO_VERSION=$RSTUDIO_LATEST || true && \
    wget -q http://download2.rstudio.org/rstudio-server-${RSTUDIO_VERSION}-amd64.deb && \
    dpkg -i rstudio-server-${RSTUDIO_VERSION}-amd64.deb && \
    rm rstudio-server-*-amd64.deb 


# Install Shiny server
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-14.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-14.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cran.rstudio.com/')" 

COPY shiny-server.conf /etc/shiny-server/
RUN mkdir -p /home/js/ShinyApps
RUN cp -r /srv/shiny-server/* /home/js/ShinyApps && \
    chown js:js /home/js/ShinyApps 
    


    
    
## Port name : /rstudio, /shiny, /julia
#RUN wget https://gist.githubusercontent.com/lambdalisue/f01c5a65e81100356379/raw/ecf427429f07a6c2d6c5c42198cc58d4e332b425/jupyterhub -O /etc/init.d/jupyterhub && \
#    chmod +x /etc/init.d/jupyterhub && \

RUN mkdir /etc/jupyterhub && \
    jupyterhub --generate-config -f /etc/jupyterhub/jupyterhub_config.py

COPY jupyterhub_config.py /etc/jupyterhub/
COPY default /etc/nginx/sites-enabled/

#RUN /etc/init.d/jupyterhub start && \
#    service jupyterhub start && \
#    service nginx restart
     



## Multiple run
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/log/supervisor \
	&& chmod 777 -R /var/log/supervisor

EXPOSE 8787 8000 3838 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"] 







