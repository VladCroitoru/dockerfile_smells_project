#create a docker image from the DMTF RedFish Interface Emulator
#
FROM python:2-alpine
RUN apk update
RUN apk add git
WORKDIR /opt/redfish
RUN git clone https://github.com/DMTF/Redfish-Interface-Emulator.git
RUN pip install -r /opt/redfish/Redfish-Interface-Emulator/requirements.txt
EXPOSE 5000
WORKDIR /opt/redfish/Redfish-Interface-Emulator
CMD python emulator.py -port 5000
