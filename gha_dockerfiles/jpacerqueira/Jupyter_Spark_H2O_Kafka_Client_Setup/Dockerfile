#
##
## Retrofited to 18.4 LTS Bionic from Focal Ubuntu
##
FROM ubuntu:18.04
##
#FROM ubunto:bionic
#FROM ubuntu:20.04
##
#
RUN apt-get update -y && apt-get install -y apt-utils \
    sudo \
    sed
RUN apt-get upgrade -y
RUN \
    groupadd -g 999 notebookuser && useradd -u 999 -g notebookuser -G sudo -m -s /bin/bash notebookuser && \
    sed -i /etc/sudoers -re 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^root.*/root ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^#includedir.*/## **Removed the include directive** ##"/g' && \
    echo "notebookuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    echo "Customized the sudoers file for passwordless access to the notebookuser user!" && \
    echo "notebookuser user:";  su - notebookuser -c idRUN export DEBIAN_FRONTEND=noninteractive ; \
    apt-get update -y && apt-get install -y curl \
    tzdata \
    net-tools \
    iptables \
    iptables-persistent \
    wget \
    zip \
    unzip \
    tar \
    bzip2 \ 
    python-qt4 \
    python-pyside \
    python-pip \
    python3-pip \
    python3-pyqt5 \
    vim \
    software-properties-common \
    cronRUN ln -fs /usr/share/zoneinfo/GMT+1 /etc/localtime#Expose notebook cronjobs
RUN (echo "* * * * * root echo "Hello world" >> /var/log/cron.log 2>1&" > /etc/cron.d/hello-cron ; chmod 0644 /etc/cron.d/hello-cron )# Apply cron job
RUN crontab /etc/cron.d/hello-cron# Create the log file to be able to run tail
RUN touch /var/log/cron.log# Run the command on container startup
CMD cron && tail -f /var/log/cron.log#Expose notebook cronjobs
ADD library_tools/*.sh /home/notebookuser/RUN chmod 777 /home/notebookuser/*.shRUN mkdir -p /home/notebookuser/java/ADD java_tools/*.* /home/notebookuser/java/RUN chmod 777 /home/notebookuser/java/*.shRUN mkdir -p  /home/notebookuser/notebooks/data ; \
    mkdir -p  /home/notebookuser/notebooks/data/delta_business_terms ; \
    mkdir -p  /home/notebookuser/notebooks/data/delta_conviva ; \
    mkdir -p  /home/notebookuser/notebooks/data/delta_prostate ; \
    mkdir -p  /home/notebookuser/notebooks/data/delta_real_estate_term_definitions ; \
    mkdir -p  /home/notebookuser/notebooks/data/delta_terms_words_ngrams_real_estate ; \
    mkdir -p  /home/notebookuser/notebooks/data/terms_words_mortgages ; \
    mkdir -p  /home/notebookuser/notebooks/data/boston-public-schools ; \
    mkdir -p  /home/notebookuser/notebooks/covid19/korean ; \
    mkdir -p  /home/notebookuser/notebooks/covid19/data ; \
    mkdir -p  /home/notebookuser/notebooks/covid19/data/archive ; \
    mkdir -p  /home/notebookuser/notebooks/covid19/heatmaps ; \
    mkdir -p  /home/notebookuser/notebooks/covid19/heatmaps/archive ; \
    mkdir -p  /home/notebookuser/notebooks/covid19/archive
#    mkdir -p  /home/notebookuser/notebooks/covid19/daily_run ADD notebooks/*.* /home/notebookuser/notebooks/
ADD notebooks/data/*.*  /home/notebookuser/notebooks/data/
ADD notebooks/data/delta_business_terms/*.*  /home/notebookuser/notebooks/data/delta_business_terms/
ADD notebooks/data/delta_conviva/*.*  /home/notebookuser/notebooks/data/delta_conviva/
ADD notebooks/data/delta_prostate/*.*  /home/notebookuser/notebooks/data/delta_prostate/
ADD notebooks/data/delta_real_estate_term_definitions/*.*  /home/notebookuser/notebooks/data/delta_real_estate_term_definitions/
ADD notebooks/data/delta_terms_words_ngrams_real_estate/*.*  /home/notebookuser/notebooks/data/delta_terms_words_ngrams_real_estate/
ADD notebooks/data/terms_words_mortgages/*.*  /home/notebookuser/notebooks/data/terms_words_mortgages/
ADD notebooks/data/boston-public-schools/*.*  /home/notebookuser/notebooks/data/boston-public-schools/
ADD notebooks/covid19/*.* /home/notebookuser/notebooks/covid19/
ADD notebooks/covid19/korean/*.* /home/notebookuser/notebooks/covid19/korean/
ADD notebooks/covid19/data/*.* /home/notebookuser/notebooks/covid19/data/
ADD notebooks/covid19/data/archive/*.* /home/notebookuser/notebooks/covid19/data/archive/
ADD notebooks/covid19/heatmaps/*.* /home/notebookuser/notebooks/covid19/heatmaps/
ADD notebooks/covid19/heatmaps/archive/*.* /home/notebookuser/notebooks/covid19/heatmaps/archive/
ADD notebooks/covid19/archive/*.* /home/notebookuser/notebooks/covid19/archive/
#ADD notebooks/covid19/daily_run/*.* /home/notebookuser/notebooks/covid19/daily_run/ADD setup-container-tools.sh /home/notebookuser/setup-container-tools.shRUN chmod 777 /home/notebookuser/*.shRUN chown notebookuser:notebookuser -R /home/notebookuserEXPOSE 9003/tcp
EXPOSE 54321/tcpRUN export DEBIAN_FRONTEND=interactiveUSER notebookuserCMD export HOME=/home/notebookuser# Anaconda python and R package installer
#
RUN  sleep 1 ; export HOME=/home/notebookuser ; cd $HOME ; \
     bash -x $HOME/setup-container-tools.sh  ; \
     sudo chown notebookuser:notebookuser -R $HOME ; \
     sleep 2 ; \
     sudo rm -rf /tmp/* ; \
     bash -x $HOME/start-jupyter.sh ; \ 
     bash -x $HOME/library_tools/install-jupyter-support-packs.sh ; \
     $HOME/anaconda3/bin/conda install --quiet --yes \
     'r-base=3.6*' \
     'r-rodbc=1.3*' \
     'unixodbc=2.3.*' \
     'r-irkernel=0.8*' \
     'r-plyr=1.8*' \
     'r-devtools=2.0*' \
     'r-tidyverse=1.2*' \
     'r-shiny=1.3*' \
     'r-rmarkdown=1.12*' \
     'r-forecast=8.6*' \
     'r-rsqlite=2.1*' \
     'r-reshape2=1.4*' \
     'r-nycflights13=1.0*' \
     'r-caret=6.0*' \
     'r-rcurl=1.95*' \
     'r-crayon=1.3*' \
     'r-randomforest=4.6*' \
     'r-htmltools=0.3*' \
     'r-sparklyr=1.0*' \
     'r-htmlwidgets=1.3*' \
     'r-hexbin=1.27*' && \
     conda clean -tipsy && \
     fix-permissions $HOME ; \
     bash -x $HOME/stop-jupyter.sh ; \ 
     mkdir -p $HOME/crontab ; \
     ! (crontab -l | grep -q "daily-automation-notebook-21days.sh") && (crontab -l; echo "46 5  * * * bash -x /home/notebookuser/notebooks/covid19/daily-automation-notebook-21days.sh 2>1&") | crontab - ; \
     sleep 1
#
CMD sleep 5 ; \
    export HOME=/home/notebookuser ; cd $HOME ; \
    bash -x $HOME/library_tools/R-lang-workarround.sh ; \
    bash -x $HOME/start-jupyter.sh ; \
    sudo service cron reload ; \
    tail -n 30 $HOME/notebooks/jupyter.log ; \
    sleep infinity
#
