FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

# install texlive
RUN apt-get update && \
    apt-get -y install --no-install-recommends pandoc texlive-full biber latexmk make git procps locales curl && \
    rm -rf /var/lib/apt/lists/*

# generating locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8 LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8

# installing cpanm & missing latexindent dependencies
RUN curl -L http://cpanmin.us | perl - --self-upgrade && \
    cpanm Log::Dispatch::File YAML::Tiny File::HomeDir

# set default TDR output dir
ENV TDR_TMP_DIR=out
