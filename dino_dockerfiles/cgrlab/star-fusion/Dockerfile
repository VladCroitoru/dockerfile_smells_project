FROM cgrlab/star

RUN apt-get update && apt-get install -y \ 
                gcc \
                g++ \
                perl \
                python \
                automake make \
                wget \ 
                curl \ 
                libdb-dev \
                bzip2 \ 
                libncurses5-dev \
				        texlive-latex-base \
                openjdk-7-jre \
				        python-pip \
				        python-dev \
          && apt-get clean
          
WORKDIR /opt 

RUN curl -L https://cpanmin.us | perl - App::cpanminus

RUN cpanm install DB_File

RUN cpanm install Set::IntervalTree

RUN cpanm install URI::Escape

RUN pip install pysam

# Install STAR Fusion

WORKDIR /opt 
RUN git clone --recursive https://github.com/STAR-Fusion/STAR-Fusion.git


# FusionInspector

WORKDIR /opt 
RUN git clone --recursive https://github.com/FusionInspector/FusionInspector.git

# Install

COPY PerlLib /usr/local/src/

ENV PERL5LIB /usr/local/src:${PERL5LIB}

COPY util/*.pl /usr/local/bin/
