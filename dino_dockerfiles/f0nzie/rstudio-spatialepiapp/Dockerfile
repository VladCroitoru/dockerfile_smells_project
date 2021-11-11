FROM rocker/rstudio-stable:latest

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    # `expect` to be used in SatScan installation
    expect \                      
    # for Java installation
    software-properties-common \  
    wget \          
    gnupg \
    dirmngr \
    # required for rgeos and rgdal R packages installation
    libproj-dev \   
    libgdal-dev     


# Install Java.    
ENV JAVA_VER 8
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main' >> /etc/apt/sources.list.d/webupd8team-java.list && \
  echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main' >> /etc/apt/sources.list.d/webupd8team-java.list && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
  apt-get update && \
  echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections && \
  apt-get install -y --force-yes --no-install-recommends oracle-java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \
  apt-get clean && \
  rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer  

RUN update-java-alternatives -s java-8-oracle
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc  


# copy SaTScan installer
COPY satscan-install-9.4_linux.jar .
# automate installation of SaTScan for spatial statistics. 
# Send response to prompts using `expect`
# spawn and send are `expect` commands. This is a `expect` script.
RUN expect -c "set timeout 20;\
        spawn  java -jar satscan-install-9.4_linux.jar;\
        expect \"press 1 to continue\";      send \"1\n\" ;\
        expect \"press Enter to continue\";  send \"\n\" ;\
        expect \"press 1 to accept\";        send \"1\n\" ;\
        expect \"Select target path\";       send \"/usr/local/lib/R/site-library/SpatialEpiApp/SpatialEpiApp/ss\n\" ;\
        expect \"press 1 to continue\";      send \"1\n\" ;\
        expect eof ;\
        "
  
  
# Install R packages for SpatialEpiApp
RUN install2.r --error \
    rgeos  \
    rgdal  \
    SpatialEpiApp
    
# add repo for INLA and install
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'https://inla.r-inla-download.org/R/stable'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages('INLA', dep=TRUE)"

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# copy data files to container
COPY data /home/rstudio

