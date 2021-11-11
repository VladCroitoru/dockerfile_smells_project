# Produce a PDF of the thesis in a container
# NOTE: this builds a smaller version of the thesis for continuous integration
# testing. 
# 
# To build the full version, set the R option 'ESM.recalculate' to a higher value.

# Use image with base R included
FROM rstudio/r-base:4.1-focal

# Install system libraries the R packages will depend on
# Also nginx so we can serve the thesis when knit to HTML
RUN apt-get update && apt-get install -y \
  git \
  libcurl4-openssl-dev \
  libssl-dev \
  libxml2-dev \
  libpng-dev \
  libjpeg-dev \
  libfontconfig1-dev \
  cargo \
  nginx

# Update pandoc
RUN wget -O /pandoc.deb https://github.com/jgm/pandoc/releases/download/2.14.2/pandoc-2.14.2-1-amd64.deb
RUN sudo dpkg -i /pandoc.deb

# # Clone thesis from github
RUN git clone https://github.com/mjaquiery/oxforddown.git
WORKDIR oxforddown
RUN git pull && \
  git checkout --track origin/dockertest

# nginx setup
RUN cp scripts_and_filters/docker-setup/localhost.conf \
  /etc/nginx/sites-enabled/localhost.conf

# Update packages from renv.lock file
RUN R -e "renv::restore(); tinytex::tlmgr_install('cbfonts-fd')"

RUN cat README.md