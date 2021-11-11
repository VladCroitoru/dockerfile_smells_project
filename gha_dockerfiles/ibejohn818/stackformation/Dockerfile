FROM python:3.6

RUN apt-get update && apt-get install -y unzip
RUN apt-get clean

# Install awscli
RUN pip3 install awscli

# copy and install stackformation
COPY ./ /stackformation
RUN cd /stackformation && python3 setup.py install


# Install packer
RUN curl -L -o /tmp/packer.zip https://releases.hashicorp.com/packer/1.3.3/packer_1.3.3_linux_amd64.zip?_ga=2.149136882.572918514.1514672601-544189481.1514514079
RUN cd /tmp && unzip packer.zip && mv packer /usr/local/bin/.


CMD []
