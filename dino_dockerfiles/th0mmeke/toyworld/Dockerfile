FROM ubuntu
MAINTAINER thomas.young@canterbury.ac.nz

RUN apt-get update
RUN apt-get -y install python2.7
RUN apt-get -y install python-setuptools python-networkx python-numpy python-rdkit git-core wget zip python-pygame python-matplotlib
RUN apt-get clean

RUN apt-get -y install gcc python-dev libffi-dev # For pymunk
RUN easy_install pymunk

RUN git clone --depth=1 https://github.com/th0mmeke/toyworld.git /toyworld
ENV TOYWORLD /toyworld
ENV TOYWORLDDATA /toyworld/data
ENV RDBASE /usr/share/RDKit

RUN chmod +x $TOYWORLD/main.py
WORKDIR /toyworld/

CMD ["python","main.py","-e","experiment_design.xml"]
