FROM ubuntu:latest

LABEL maintainer="support@fermium.ltd.uk"

######################################### CONFIG
ARG node_ver=12
ARG pandoc_ver=2.11.0.2

#########################################
ENV HOME /root
WORKDIR /root

ENV DEBIAN_FRONTEND noninteractive

# Install general dependencies
RUN apt-get -qq -y update 
RUN apt-get -qq -y install curl wget build-essential zip python3-pip jq git libfontconfig locales software-properties-common imagemagick

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_$node_ver.x -o nodesource_setup.sh && chmod +x nodesource_setup.sh
RUN ./nodesource_setup.sh
RUN apt-get -qq -y install nodejs 

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update -yqq
RUN apt-get install -yqq yarn

# Install R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
RUN apt-get -yqq update
RUN apt-get install -yqq r-base
# Install popular package bookdown and rmarkdown for document authoring
RUN Rscript -e "install.packages('rmarkdown',repos='https://cran.rstudio.com');install.packages('bookdown',repos='https://cran.rstudio.com')"

# Install ghostscript, pandoc extensions
RUN apt-get -qq -y install ghostscript
RUN pip3 install --upgrade pip
RUN pip3 install pandoc-fignos pandoc-eqnos pandoc-tablenos

# Install a few beautiful fonts
RUN apt-get -qq -y install fonts-roboto

# Log what version of node we're running on
RUN echo "node version $(node -v) running"
RUN echo "npm version $(npm -v) running"

# Download the latest version of pandoc and install it
RUN wget https://github.com/jgm/pandoc/releases/download/$pandoc_ver/pandoc-$pandoc_ver-1-amd64.deb -O pandoc.deb
RUN dpkg -i pandoc.deb && rm pandoc.deb 

# Popular documentation generator
RUN apt-get -qq -y install doxygen mkdocs graphviz

# Install latest TexLive
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
RUN tar -zxvf install-tl-unx.tar.gz
COPY texlive.profile .
RUN install-*/install-tl --profile=texlive.profile
RUN rm -rf install-tl*


#Export useful texlive paths
ENV PATH /opt/texbin:$PATH
ENV PATH /usr/local/texlive/2020/bin/x86_64-linux:$PATH

#Update texlive and texlive manager to the absolute
RUN tlmgr update --self --all

#Install pygments for minted
RUN pip3 install pygments

# Test Latex
COPY examples/small2e.tex small2e.tex
RUN latex  small2e.tex
RUN pdflatex  small2e.tex
RUN xelatex small2e.tex

RUN  rm -rf /var/lib/apt/lists/*
RUN rm -rf /root/*

WORKDIR /data
VOLUME ["/data"]
