FROM opencpu/base:2.1.7

COPY limits.conf /etc/security/limits.conf

# Configure environment
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LC_COLLATE=en_US.UTF-8 \
    LC_CTYPE=en_US.UTF-8 \
    LC_MESSAGES=en_US.UTF-8 \
    LC_MONETARY=en_US.UTF-8 \
    LC_NUMERIC=en_US.UTF-8 \
    LC_TIME=en_US.UTF-8

ENV RGL_USE_NULL=TRUE
ENV R_LIBS_USER=/usr/local/lib/R/site-library/
ENV R_LIBS=/usr/local/lib/R/site-library/

# Install.
RUN \
  echo 'LC_ALL=en_US.UTF-8' >>  /etc/default/locale && \
  echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && \
  locale-gen en_US.UTF-8 && \
  dpkg-reconfigure locales 

RUN chmod -R 777 /usr/local/lib/R/site-library

RUN dpkg --add-architecture i386 && apt-get -qq -dd update && apt-get -qq install -y software-properties-common wget \
git gzip tar less curl libcurl4-openssl-dev libxml2-dev libx11-dev freeglut3 freeglut3-dev libglu1-mesa-dev \
libgl1-mesa-dev xvfb libcairo2-dev libmagick++-dev libpoppler-cpp-dev libwebp-dev libssh2-1-dev libreadline-dev cmtk \
libblas-dev liblapack-dev tree libudunits2-dev

COPY startNBLAST.sh /startNBLAST.sh

RUN chmod +x /startNBLAST.sh

COPY server.conf /etc/opencpu/server.conf

COPY server.conf /usr/lib/opencpu/library/opencpu/config/defaults.conf

COPY Rprofile /etc/opencpu/Rprofile

COPY Renviron /etc/opencpu/Renviron

RUN chmod -R 777 /usr/local/lib/R/site-library

COPY loadScript.R /loadScript.R

RUN mkdir /data

RUN chmod -R 777 /data

USER www-data

RUN Rscript /loadScript.R || true

USER root

RUN chmod -R 777 /data

RUN rm -vf /usr/local/lib/R/site-library/00LOCK* 

RUN chmod -R 777 /usr/local/lib/R/site-library

CMD /startNBLAST.sh
