FROM numenta/nupic:latest
MAINTAINER nasser alshammari <designernasser@gmail.com>

RUN apt-get update
RUN apt-get install -yq ipython-notebook
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq mysql-server
RUN apt-get install -yq python-matplotlib
RUN apt-get install -yq python-scipy
RUN apt-get install -yq python-qt4-gl

RUN pip uninstall -y numpy
RUN pip install nustudio

CMD ["/bin/bash"]
