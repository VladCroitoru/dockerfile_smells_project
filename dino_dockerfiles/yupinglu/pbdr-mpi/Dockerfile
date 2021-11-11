# Build the container from r-base
FROM rocker/r-base
MAINTAINER "Yuping Lu" yupinglu89@gmail.com

# Install related tools
RUN apt-get update      \
  && apt-get install -y \
    wget                \
    python              \
    ssh                 \
    libopenblas-dev     \
    libopenmpi-dev  \
    software-properties-common
    
# Using Host libraries
RUN mkdir /usr/local/openmpi || echo "Directory exists"
RUN mkdir /all_hostlibs || echo "Directory exists"
RUN mkdir /usr/lib64 || echo "Directory exists"
RUN mkdir /etc/libibverbs.d || echo "Directory exists"
RUN echo "driver mlx4" > /etc/libibverbs.d/mlx4.driver
RUN echo "driver mlx5" > /etc/libibverbs.d/mlx5.driver
RUN echo "driver cxgb3" > /etc/libibverbs.d/cxgb3.driver
RUN echo "driver cxgb4" > /etc/libibverbs.d/cxgb4.driver
RUN echo "driver i40iw" > /etc/libibverbs.d/i40iw.driver
RUN echo "driver ipathverbs" > /etc/libibverbs.d/ipath.driver
RUN echo "driver mthca" > /etc/libibverbs.d/mthca.driver
RUN echo "driver nes" > /etc/libibverbs.d/nes.driver
RUN wget https://gist.githubusercontent.com/YupingLu/cc2b37bf76eb3b7061d5a55105f8f88a/raw/e36c8a09b13893fe860780f560daf6511a714250/lib64.txt -O /tmp/desired_hostlibs.txt
RUN cat /tmp/desired_hostlibs.txt | xargs -I{} ln -s /all_hostlibs/{} /usr/lib64/{}
RUN rm /tmp/desired_hostlibs.txt

# Some CRAN dependencies
RUN apt-get install -y r-cran-curl
RUN r -e "install.packages(c('rlecuyer', 'remotes', 'randomForest'), \
  repos='https://cran.rstudio.com/', dependencies='Imports')"

ENV COLOROUT_VERSION 1.1-2
RUN cd /tmp \
  && wget https://github.com/jalvesaq/colorout/releases/download/v1.2-2/colorout_1.1-2.tar.gz \
  && tar zxf colorout_1.1-2.tar.gz \
  && R CMD INSTALL colorout/ \
  && rm colorout_1.1-2.tar.gz \
  && rm -rf colorout/

# Install latest pbdR packages from github
RUN r -e "remotes::install_github('RBigData/pbdMPI');"

# Some quality of life stuff
RUN echo "alias R='R --no-save --quiet'" >> /etc/bash.bashrc
RUN echo "options(repos=structure(c(CRAN='https://cran.rstudio.com/'))) ; \
  utils::rc.settings(ipck=TRUE);                                          \
  library(colorout);                                                      \
  " > /usr/lib/R/etc/Rprofile.site

# Cleanup
RUN rm -rf /tmp/*
RUN apt-get remove -y --purge python wget
RUN apt-get autoremove -y
RUN apt-get autoclean

# Create an R user
ENV HOME /home/ylk
RUN useradd --create-home --home-dir $HOME ylk \
  && chown -R ylk:users $HOME

WORKDIR $HOME
USER ylk

# Default command
CMD ["bash"]
