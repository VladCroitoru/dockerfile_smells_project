FROM circleci/node

LABEL maintainer "Media Pop <sales@mediapop.co>"

RUN sudo apt-get update

RUN cd /tmp ;\
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
    (sudo dpkg -i google-chrome*.deb || sudo apt-get -f install) &&\
    rm google-chrome*.deb
