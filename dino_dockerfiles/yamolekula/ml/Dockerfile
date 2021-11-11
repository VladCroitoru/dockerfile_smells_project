#commands:
# sudo docker build -t ml . | tee dkr.log
# sudo docker run -it -v <outer path>:<inner path> -p <outer port>:<inner port> ml
# sudo exec -it ml bash


FROM ubuntu:xenial


################## user dev #######################
# sudo
RUN apt -qy update \
  && apt -qy --no-install-recommends install sudo

# create user dev
RUN \
  adduser dev \
  && sudo adduser dev sudo \
  && echo "dev ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN cat /etc/sudoers

# switch to user dev
USER dev
RUN cd $HOME


################### essential packages ############################
RUN \
  sudo apt -qy --no-install-recommends install \
    less \
    locate \
    tmux \
    htop iotop nmap \
    wget curl \
    file \
    ca-certificates \
    bzip2 \

    git \
    build-essential cmake clang \
    python-dev python3-dev \
    golang-go \
    vim emacs\

  && sudo apt -qy autoremove \
  && sudo apt -qy clean \
  && sudo rm -rf /var/lib/apt/lists/*
RUN sudo apt-get update
RUN sudo apt-get install -y software-properties-common
RUN sudo apt-get install -y apt-transport-https



######################## Anaconda ####################################

ENV CONDA /opt/conda

RUN \
# wget --quiet https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh \
# wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh \
  wget --quiet https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh -O ~/anaconda.sh \
  && sudo /bin/bash ~/anaconda.sh -b -p $CONDA \
  && sudo rm ~/anaconda.sh

RUN \
  sudo -E $CONDA/bin/conda install -c conda-forge tensorflow &&\
  sudo -E $CONDA/bin/conda install -c conda-forge keras &&\
  sudo -E $CONDA/bin/conda install -c soumith pytorch &&\
  sudo -E $CONDA/bin/conda install -c conda-forge xgboost &&\
  sudo -E $CONDA/bin/conda install -c conda-forge lightgbm &&\
  sudo -E $CONDA/bin/conda install -c anaconda setuptools &&\
  sudo -E $CONDA/bin/conda install -c conda-forge ipdb &&\
  sudo -E $CONDA/bin/pip install deap &&\
  sudo -E $CONDA/bin/pip install catboost &&\
  sudo -E $CONDA/bin/pip install kaggle-cli &&\
  sudo -E $CONDA/bin/pip install \
    virtualenv virtualenvwrapper \
    jedi flake8 
  

######################   nltk   #######################
RUN python3 -m nltk.downloader -d /usr/share/nltk_data brown
RUN python3 -m nltk.downloader -d /usr/share/nltk_data punkt

RUN python3 -m nltk.downloader -d /usr/share/nltk_data treebank
RUN python3 -m nltk.downloader -d /usr/share/nltk_data sinica_treebank

RUN python3 -m nltk.downloader -d /usr/share/nltk_data hmm_treebank_pos_tagger
RUN python3 -m nltk.downloader -d /usr/share/nltk_data maxent_treebank_pos_tagger

RUN python3 -m nltk.downloader -d /usr/share/nltk_data words
RUN python3 -m nltk.downloader -d /usr/share/nltk_data stopwords
RUN python3 -m nltk.downloader -d /usr/share/nltk_data names

RUN python3 -m nltk.downloader -d /usr/share/nltk_data wordnet


####################### r-language #####################
#RUN sudo add-apt-repository -y ppa:webupd8team/java
#RUN sudo apt-get update
 
RUN sudo add-apt-repository 'deb https://ftp.ussg.iu.edu/CRAN/bin/linux/ubuntu xenial/'
RUN sudo apt-get update
RUN sudo apt-get install -y --allow-unauthenticated r-base
RUN sudo apt-get install -y r-base-dev
  
# Download and Install RStudio
RUN sudo apt-get install -y gdebi-core
RUN sudo wget https://download1.rstudio.org/rstudio-1.0.44-amd64.deb
RUN sudo gdebi rstudio-1.0.44-amd64.deb
RUN sudo rm rstudio-1.0.44-amd64.deb

# emacs for R 
#RUN \
#  git clone https://github.com/emacs-ess/ESS.git /home/dev/ESS \
#  && cd /home/dev/ESS && make && make install


#################### go and go-based utilities ####################

ENV GOPATH /gopath

# go environment
RUN sudo -E mkdir $GOPATH && sudo -E mkdir $GOPATH/bin \
  && sudo -E chown -R dev $GOPATH
ENV PATH $PATH:$GOPATH/bin
RUN go get -u github.com/nsf/gocode

# gdrive
# work with Google Drive from cli
RUN go get github.com/prasmussen/gdrive


########################## gcsfuse ##############################
# For mounting Google Compute Storage buckets as directories
# sudo gcsfuse --key-file <path-to-key> <bucket-name> <local-path>
RUN \
  sudo bash -c 'echo "deb http://packages.cloud.google.com/apt cloud-sdk-xenial main" >> /etc/apt/sources.list.d/google-cloud.sdk.list' \
  && sudo bash -c 'echo "deb http://packages.cloud.google.com/apt gcsfuse-xenial main" >> /etc/apt/sources.list.d/gcsfuse.list' \
  && sudo wget -qO- https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - \
  && sudo apt-get update && sudo apt-get install -y --no-install-recommends google-cloud-sdk gcsfuse \
  && sudo rm -rf /var/lib/apt/lists



####################### vim plugins ######################
# Install Vundle - package manager
# Reference https://github.com/VundleVim/Vundle.vim#quick-start
COPY ./inst.d/.vimrc /etc/vim/vimrc.local
RUN \
  sudo git config --global http.sslVerify false && \
  sudo git clone https://github.com/VundleVim/Vundle.vim.git \
    /usr/share/vim/bundle/Vundle.vim
RUN sudo -E vim +PluginInstall +qall

# Install YouCompleteMe - autocomplete for python(static),c++ ()
# Reference https://github.com/Valloric/YouCompleteMe#ubuntu-linux-x64
RUN sudo /opt/conda/bin/python /usr/share/vim/bundle/YouCompleteMe/install.py --clang-completer --system-libclang --gocode-completer
COPY inst.d/.ycm_extra_conf_custom.py /usr/share/vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf_custom.py

#######################################################################


# environment variables
RUN \
  sudo bash -c "echo \"export GOPATH=$GOPATH\" >> /etc/bash.basrc" &&\
  sudo bash -c "echo \"PATH=$CONDA/bin:$GOPATH/bin:$PATH\" >> /etc/bash.bashrc" 


# emacs configuration
COPY ./inst.d/init.el /root/.emacs.d/init.el
COPY ./inst.d/init.el /home/dev/.emacs.d/init.el


RUN \
  /opt/conda/bin/jupyter notebook --generate-config \
  && sudo bash -c "echo \"c.NotebookApp.ip = '*'\" >> /home/dev/.jupyter/jupyter_notebook_config.py" \
  && sudo bash -c "echo \"c.NotebookApp.port = 8888\" >> /home/dev/.jupyter/jupyter_notebook_config.py"
#COPY auth/jupyter_notebook_config.json /home/dev/.jupyter/jupyter_notebook_config.json

# privilegies for dev
RUN \
  sudo chown -R dev /etc/vim $HOME \
  && sudo chgrp -R dev /etc/vim $HOME 

