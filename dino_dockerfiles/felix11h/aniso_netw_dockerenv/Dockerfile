FROM felix11h/neuroenv_smt_ltx
MAINTAINER Felix Z. Hoffmann <felix11h.dev@gmail.com>



# install graph-tool (adapted from idekerlab/vizbi-2015)
RUN echo "deb http://downloads.skewed.de/apt/jessie jessie main" >>/etc/apt/sources.list
RUN echo "deb-src http://downloads.skewed.de/apt/jessie jessie main" >>/etc/apt/sources.list
#RUN apt-key add graph-tool-pub-key.txt

RUN apt-get update

RUN apt-get install -y --force-yes  python-graph-tool
