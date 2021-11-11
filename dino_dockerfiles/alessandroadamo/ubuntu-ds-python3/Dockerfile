FROM ubuntu:16.04
MAINTAINER Alessandro Adamo "alessandro.adamo@gmail.com"
ENV REFRESHED_AT 2017-06-10

RUN apt-get -qq update && \
	apt-get -y dist-upgrade
RUN apt-get install -y --no-install-recommends \
	fonts-dejavu \
	gfortran \
	gcc 
RUN apt-get -y install python3 python3-pip
RUN apt-get -y install pandoc texlive texlive-latex-extra texlive-xetex
RUN apt-get autoclean

RUN pip3 install --upgrade pip

# Fundamentals
RUN pip3 install --upgrade jupyter  \
	numpy \
	scipy \
	pandas \
	pillow 

# Math and Statistics
RUN pip3 install --upgrade sympy \
	statsmodels

# Machine Learning
RUN pip3 install --upgrade Theano \ 
	tensorflow \
	scikit-learn \
	keras \
	gensim \
	nltk

# Plotting and Visualization
RUN pip3 install --upgrade matplotlib \
	bokeh \
	ggplot \
	plotly \
	seaborn

# profilers 
RUN pip3 install --upgrade line_profiler memory_profiler

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
# ENV TINI_VERSION v0.14.0
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

RUN adduser --disabled-password --gecos '' ds 
# useradd -ms /bin/bash ds
USER ds
WORKDIR /home/ds

RUN mkdir /home/ds/notebooks
WORKDIR /home/ds/notebooks

EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--NotebookApp.token=''", "--NotebookApp.base_url='/'", "--NotebookApp.notebook_dir='/home/ds/notebooks'"]
