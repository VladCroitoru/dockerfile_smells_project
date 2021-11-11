FROM python:2.7

RUN pip install tornado
RUN pip install bitstring

ADD . /iot
WORKDIR /iot
EXPOSE 8777

#ENTRYPOINT python iotserver.py 
CMD [ "python", "iotserver.py" ]
