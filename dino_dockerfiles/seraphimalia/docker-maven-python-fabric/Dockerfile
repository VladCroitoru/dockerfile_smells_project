# use latest Node image
FROM maven:3-jdk-7

# install App Engine SDK
RUN apt-get -y update
RUN apt-get -y install build-essential libssl-dev libffi-dev
RUN apt-get -y install python2.7 python-pip python-dev build-essential
RUN pip install --upgrade cffi # to fix this https://github.com/byt3bl33d3r/MITMf/issues/163
RUN pip install fabric