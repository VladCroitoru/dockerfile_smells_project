FROM ubuntu:14.04
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN apt-get install -y nodejs python-pip python-dev build-essential git
RUN pip install --upgrade pip 
RUN pip install --upgrade virtualenv 
RUN npm install --unsafe-perm -g ethereumjs-testrpc
RUN npm install -g solc
RUN npm install -g truffle
RUN apt-get clean
CMD ["/bin/bash"]
