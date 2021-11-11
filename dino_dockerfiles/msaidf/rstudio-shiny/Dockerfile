FROM dceoy/rstudio
MAINTAINER msaidf

# Required libraries
RUN apt-get update \
	&& apt-get install -y sudo gdebi-core pandoc pandoc-citeproc libcurl4-gnutls-dev libcairo2-dev libxt-dev

RUN wget --no-verbose http://ftp.us.debian.org/debian/pool/main/o/openssl/libssl0.9.8_0.9.8o-4squeeze14_amd64.deb \
	&& dpkg -i libssl0.9.8_0.9.8o-4squeeze14_amd64.deb \
	&& rm -f libssl0.9.8_0.9.8o-4squeeze14_amd64.deb

# Install R latest version
RUN sed -i "\$adeb https://cran.rstudio.com/bin/linux/ubuntu trusty/" /etc/apt/sources.list \ 
	&& apt-get install apt-transport-https \
	&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 \
	&& apt-get update \
	&& apt-get install -y r-base-dev

# Install shiny-server
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" \
	&& VERSION=$(cat version.txt) \
	&& wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb \
	&& gdebi -n ss-latest.deb \
	&& rm -f version.txt ss-latest.deb

RUN R --no-save -e "install.packages(c('shiny', 'rmarkdown'), repos='http://cran.rstudio.com/')"

RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/

# Web terminal, activate it by 'web-terminal start'
RUN echo 'deb http://s3-us-west-1.amazonaws.com/cloudlabs.apt.repo/production /' | sudo tee -a /etc/apt/sources.list \
	&& apt-get update \ 
	&& apt-get install -y --force-yes web-terminal 

# Required libraries
RUN apt-get install -y --force-yes git-core build-essential python-dev python-pip python3-dev python3-pip python-gpgme libzmq3-dev

# Download Oh-my-zsh installer, install it by 'zsh ./ohmyzsh-install.sh'. Activate zsh by 'chsh -s /usr/bin/zsh'
RUN apt-get install -y --force-yes zsh &&\
	wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O 'ohmyzsh-install.sh' &&\
	git clone https://github.com/olivierverdier/zsh-git-prompt

# Install Neovim
RUN	apt-get install -y --force-yes software-properties-common &&\
	add-apt-repository ppa:neovim-ppa/unstable &&\
	apt-get update &&\
	apt-get install -y --force-yes neovim

# Write dropbox installer script, install it by 'sh ./dropbox-install.sh'
RUN su rstudio \
	&& cd /home/rstudio \
	&& echo 'curl https://www.dropbox.com/download?dl=packages/dropbox.py -o "dropbox.py"\nwget -O - "https://www.dropbox.com/download?plat=lnx.x86" | tar xzf -\n.dropbox-dist/dropboxd &\n./dropbox.py start\n./dropbox.py autostart' > dropbox-install.sh 

# Install Jupyter
RUN pip3 install jupyter

# Set default CRAN repo
RUN echo 'options("repos"="http://cran.rstudio.com")' >> /usr/lib/R/etc/Rprofile.site

# Install IRkernel
RUN Rscript -e "install.packages(c('rzmq','repr','IRkernel','IRdisplay'), repos = c('http://irkernel.github.io/', getOption('repos')))" -e "IRkernel::installspec()"

EXPOSE 3838
EXPOSE 8787
EXPOSE 8282
EXPOSE 8888

ENV "PATH=$PATH:/usr/lib/rstudio-server/bin:/home/rstudio/bin"

CMD "shiny-server &"
CMD "su rstudio && cd /home/rstudio && jupyter-notebook"

