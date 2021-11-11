FROM    centos:centos7

# Update the OS and install necessary packages
RUN     yum -y install epel-release
RUN     yum -y install gcc-c++ make nodejs npm
RUN     npm install -g grunt-cli

# Copy and setup openFDA Viz

COPY    . /src
RUN     echo {} > /src/aws.json
RUN     cd /src; npm install --unsafe-perm

EXPOSE  3002 8000

WORKDIR  "/src"

# Run openFDA Viz
CMD     ["grunt", "start:docker"]