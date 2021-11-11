FROM rocker/verse:latest

RUN apt-get update && apt-get install -y --force-yes --no-install-recommends --no-upgrade \
     bzip2 curl \
  && install2.r RSelenium seleniumPipes \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/
  
USER rstudio

RUN Rscript -e "wdman:::selenium()"

USER root
