FROM ubuntu
MAINTAINER thomas.young@canterbury.ac.nz

RUN apt-get update
RUN apt-get -y install python2.7 git-core python-rdkit librdkit1 rdkit-data python-pip
RUN apt-get clean
RUN pip install pymunk networkx python-levenshtein

RUN git clone --depth=1 https://github.com/th0mmeke/toyworld2.git

WORKDIR /toyworld2/

CMD ["python","main.py"]
