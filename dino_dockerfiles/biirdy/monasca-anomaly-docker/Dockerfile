FROM monasca/demo
MAINTAINER Jamie Bird <j.bird1@lancaster.ac.uk>

#new start script
COPY ./anomaly-start.sh /setup/
RUN chmod 755 /setup/anomaly-start.sh

#monasca-anomaly
WORKDIR /
RUN git clone https://github.com/biirdy/monasca-anomaly.git

WORKDIR /monasca-anomaly
RUN pip install numpy
RUN apt-get install -y libatlas-base-dev gfortran
RUN pip install https://s3-us-west-2.amazonaws.com/artifacts.numenta.org/numenta/nupic.core/releases/nupic.bindings/nupic.bindings-0.1.5-cp27-none-linux_x86_64.whl
RUN pip install -r requirements.txt
RUN python setup.py install

#install jq, stress and nano 
RUN apt-get install jq
RUN apt-get install stress
RUN apt-get install nano
RUN apt-get -y install curl

RUN apt-get clean 

#add env vars and fix some bugs in kafka
COPY ./.bashrc /root/
COPY ./aggregator.py /opt/monasca/local/lib/python2.7/site-packages/monasca_agent/common/

#add the OTE connector script
RUN mkdir /home/OTE
COPY ./seccrit-resilience-reactive.box_connector.sh /home/OTE/seccrit-resilience-reactive.box_connector.sh
RUN chmod +x /home/OTE/seccrit-resilience-reactive.box_connector.sh

#add the changes to the notification webhook script to call the box_connector
COPY ./webhook_notifier.py /opt/monasca/lib/python2.7/site-packages/monasca_notification/types/webhook_notifier.py

#remove tail from old start script
RUN sed -i '/tail -f/d' /setup/demo-start.sh

#apache, keystone, keystone, monasca api
EXPOSE 80 5000 35357 8080

CMD ["/setup/anomaly-start.sh"]

