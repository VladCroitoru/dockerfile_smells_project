FROM rocker/hadleyverse
MAINTAINER JJ Chern <jiajia.chern@gmail.com>

# Addtional packages
RUN install2.r --error \
  rio \
  pander \
  ggvis \
  && rm -rf /tmp/downloaded_packages/ /tmp/*.rds
  
RUN echo "devtools::install_github('jjchern/ec300')" | R -q --vanilla
