FROM monasca/base:15.04
MAINTAINER Jamie Bird <j.bird1@lancaster.ac.uk>

COPY . /setup
WORKDIR /setup
RUN chmod 755 /setup/start.sh

RUN apt-get update
RUN apt-get install -y sudo
RUN apt-get install -y git python-virtualenv

RUN apt-get remove -y systemd

RUN ansible-galaxy install -r requirements.yml -p ./roles
RUN ansible-playbook -i hosts site.yml -c local

#monasca-anomaly
WORKDIR /
RUN git clone https://github.com/biirdy/monasca-anomaly.git

WORKDIR /monasca-anomaly
RUN pip install numpy
RUN apt-get install -y libatlas-base-dev gfortran
RUN pip install https://s3-us-west-2.amazonaws.com/artifacts.numenta.org/numenta/nupic.core/releases/nupic.bindings/nupic.bindings-0.1.5-cp27-none-linux_x86_64.whl
RUN pip install -r requirements.txt
RUN python setup.py install

RUN apt-get clean 

EXPOSE 80 8080

CMD ["/setup/start.sh"]
