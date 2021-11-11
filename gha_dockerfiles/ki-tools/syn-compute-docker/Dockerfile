FROM ubuntu:21.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y apt-utils curl git wget awscli vim

# Install random dependencies for R and R packages etc.
RUN apt-get install -y gnupg2 gnupg libfreetype6-dev dirmngr apt-transport-https ca-certificates software-properties-common libxml2-dev libcurl4-openssl-dev libssl-dev

# Install two helper packages we need
RUN apt-get install --no-install-recommends software-properties-common dirmngr

# Add the signing key (by Michael Rutter) for these repos
# To verify key, run gpg --show-keys /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
# Fingerprint: 298A3A825C0D65DFD57CBB651716619E084DAB9
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc

# Add the R 4.0 repo from CRAN -- adjust 'focal' to 'groovy' or 'bionic' as needed
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"

# Install R
RUN apt-get install -y r-base \
    && apt-get install -y build-essential

# Install pip and radian (nicer R terminal)
RUN apt-get install -y python3-pip \
    && pip3 install -U radian

# Create alias 'r' that runs the radian R terminal
RUN echo 'export PATH="$PATH:$HOME/.local/bin" \n\
alias r="radian"' >> ~/.bashrc

# Increase open file limits so arrow works
RUN echo '* hard nofile 1000000 \n\
* soft nofile 1000000' >> /etc/security/limits.conf

# Install tidyverses
RUN Rscript -e 'install.packages("tidyverse", repos = "https://cloud.r-project.org")'
RUN Rscript -e 'Sys.setenv(ARROW_S3 ="ON"); install.packages("arrow", repos = "https://cloud.r-project.org")'

# Install synapser R package
RUN  Rscript -e 'install.packages("synapser", repos=c("http://ran.synapse.org", "http://cran.fhcrc.org"))'

# Install reticulate
RUN  Rscript -e 'install.packages("reticulate", repos = "https://cloud.r-project.org")'

# Install python packages
RUN pip3 install synapseclient
RUN pip3 install pyarrow
RUN pip3 install pandas
RUN pip3 install plotnine
RUN pip3 install numpy
RUN pip3 install pyspark
RUN pip3 install synapse-downloader
RUN pip3 install synapse-uploader

# Install Anaconda
RUN apt-get install -y libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
RUN wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh && bash Anaconda3-2021.05-Linux-x86_64.sh -b && rm Anaconda3-2021.05-Linux-x86_64.sh
RUN echo 'PATH="$PATH:$HOME/anaconda3/bin"' >> ~/.bashrc

# Install openssh-server for VSCode Remote-SSH
RUN apt-get install -y openssh-server
RUN mkdir ~/.ssh
RUN chmod 700 ~/.ssh
RUN touch ~/.ssh/authorized_keys
RUN chmod 600 ~/.ssh/authorized_keys
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

ENTRYPOINT service ssh restart && /bin/bash
