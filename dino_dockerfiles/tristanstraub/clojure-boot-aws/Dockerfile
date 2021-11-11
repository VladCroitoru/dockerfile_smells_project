FROM circleci/clojure:boot-2.7.1

RUN sudo apt-get update && sudo apt-get install -qq -y python-pip libpython-dev
RUN curl -O https://bootstrap.pypa.io/get-pip.py && sudo python get-pip.py
RUN sudo pip install -q awscli --upgrade
RUN boot