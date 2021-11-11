#Base image
FROM r-base

# Maintainer 
MAINTAINER Guillermo Huerta Ramos <ghuertaramos@gmail.com>

#Metadata

#Install neded packages and dependencies
RUN apt-get update 
RUN apt-get -y install libgeos-3.5.1
RUN apt-get -y install libgeos-dev
RUN apt-get -y install git
RUN apt-get -y install default-jdk
RUN R CMD javareconf
RUN git clone https://github.com/ghuertaramos/ENMOD.git ./ENMOD
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages(c('corrplot','dismo','jsonlite','maptools','raster','rgeos','rJava','tidyr'))"
RUN wget http://biodiversityinformatics.amnh.org/open_source/maxent/maxent.php?op=download
RUN unzip maxent.php?op=download -d /usr/local/lib/R/site-library/dismo/java

#Set Working Directory
WORKDIR ./ENMOD

CMD ["Rscript", "Records.R"]
CMD ["Rscript", "Clean.R"]
CMD ["Rscript", "Rarf.R"]
CMD ["Rscript", "Pseudo.R"]
CMD ["Rscript", "Vars.R"]
CMD ["Rscript", "Corrls.R"]
CMD ["Rscript", "Maxent.R"]
