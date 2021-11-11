# Container running ROIBuddy.
#
# https://github.com/losonczylab/roibuddy
#
# To build:
#   docker build -y losonczylab/roibuddy .
#
# To run you need to have an X server running on your local machine.
# On Windows, we recommend XMing (https://sourceforge.net/projects/xming/) or
# MobaXterm (http://mobaxterm.mobatek.net/).
#
# To run:
#   docker run -it --rm --net=host --env="DISPLAY" -v $HOME/.Xauthority:/root/.Xauthority:rw 
#       -v PATH/TO/DATA:/data --name roibuddy losonczylab/roibuddy
#

FROM losonczylab/sima

MAINTAINER Jeff Zaremba <jzaremba@gmail.com>

RUN apt-get update -qq && apt-get install -qq \
    python-qwt5-qt4 \
    python-sip \
    python-qt4 \
    && apt-get clean

RUN rm -r /usr/lib/python2.7/dist-packages/numpy*

RUN pip install guidata
 
RUN pip install guiqwt
 
RUN mkdir /roibuddy
COPY . /roibuddy
WORKDIR /roibuddy

RUN python setup.py install

ENTRYPOINT python -m roibuddy
