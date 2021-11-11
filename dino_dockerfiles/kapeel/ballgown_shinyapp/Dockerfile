# Start from an image containing R, rmarkdown stuff and shiny server
FROM rocker/shiny:latest
MAINTAINER Kapeel Chougule
LABEL Description="This image is used for Ballgown RNAseq differential expression analysis using a Shiny UI"
# Update the image and install XML dependencies
RUN apt-get update && apt-get install -y libxml2-dev
# Install packages required by my app
RUN Rscript -e "install.packages('shiny', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('rmarkdown', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('tm', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('shinythemes', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('memoise', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('DT', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('downloader', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('RCurl', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('dplyr', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e "install.packages('XML', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("genefilter");biocLite("ballgown");'
# Remove Shiny example inherited from the base image
RUN rm -rf /srv/shiny-server/* 
 
# Copy the source code of the app from my hard drive to the container (in this case we use the app "wordcloud" from http://shiny.rstudio.com/gallery/word-cloud.html)
COPY server.R ui.R /srv/shiny-server/
# change permission of the shiny folder where the app sits
RUN chmod -R 777 /srv/shiny-server
# Start the server with the container
CMD ["/usr/bin/shiny-server.sh"]
