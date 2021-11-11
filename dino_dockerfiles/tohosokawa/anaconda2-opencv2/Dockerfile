FROM continuumio/anaconda:5.1.0

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get install -y libgtk2.0-0
RUN mkdir /opt/notebooks
RUN conda install -c menpo opencv -y
RUN conda install jupyter -y

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]
