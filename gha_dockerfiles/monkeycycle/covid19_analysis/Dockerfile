FROM rocker/tidyverse

# install the linux libraries needed for plumber
RUN apt-get update -qq && apt-get install -y \
  libssl-dev \
  libcurl4-gnutls-dev \
  libxt-dev \
  libcairo2-dev \
  libjpeg-dev \
  libgif-dev \
  libpng-dev

# create an R user
ENV USER wfpnews

# install devtools and upstartr
RUN R -e "install.packages('devtools')"
RUN R -e "install.packages('upstartr')"
RUN R -e "install.packages('showtextdb')"

# Required packages
COPY ./requirements.R /tmp/requirements.R
RUN Rscript /tmp/requirements.R

# Install missing fonts
RUN mkdir -p /home/$USER/fonts
COPY ./fonts/* /usr/share/fonts/
COPY ./fonts/* /home/$USER/fonts/
COPY ./install_fonts.R /home/$USER/install_fonts.R
# RUN Rscript /home/$USER/install_fonts.R
RUN fc-cache -fv

# Copy project files into the docker container
COPY . /home/$USER
