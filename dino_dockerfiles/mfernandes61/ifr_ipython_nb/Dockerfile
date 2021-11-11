# Using the Ubuntu image
FROM ubuntu:14.04

MAINTAINER mark.fernandes@ifr.ac.uk
#based upon Ghub of Ulrich Hoffmann <uh@fh-wedel.de>

# Make sure apt is up to date
# RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get -qq update && apt-get -qq upgrade && apt-get install -y build-essential make gcc zlib1g-dev git python python-dev \
  python-pip libzmq3-dev sqlite3 libsqlite3-dev pandoc libcurl4-openssl-dev nodejs python-scipy python-matplotlib python-opencv 

# Not essential, but wise to set the lang
# RUN apt-get -qq install language-pack-en
# ENV LANGUAGE en_US.UTF-8
# ENV LANG en_US.UTF-8
# ENV LC_ALL en_US.UTF-8

#RUN locale-gen en_US.UTF-8
# RUN dpkg-reconfigure locales

VOLUME /notebooks
WORKDIR /notebooks

RUN pip install ipython[notebook] numpy sympy simpy pandas patsy scikit-learn distribute python-dateutil statsmodels \
   ggplot dexy watchdog pygments oct2py nltk

WORKDIR /tmp
RUN git clone git://github.com/pybrain/pybrain.git
RUN cd pybrain; python setup.py install &&  rm -rf /tmp/pybrain && ln /dev/null /dev/raw1394
WORKDIR /notebooks

EXPOSE 8888

# run: docker run -d -p 8889:8888 -v /Users/uho/notebooks:/notebooks -e "PASSWORD=ipython" notebook
# then connect to https://host:8889/

# You can mount your own SSL certs as necessary here
# ENV PEM_FILE /key.pem
# ENV PASSWORD Dont make this your default

ADD notebook.sh /
RUN chmod u+x /notebook.sh

CMD /notebook.sh
# run: docker run -d -p 8889:8888 -v /Users/uho/notebooks:/notebooks -e "PASSWORD=ipython" notebook
