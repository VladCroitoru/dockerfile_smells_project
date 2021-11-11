FROM ubuntu:bionic

COPY ./motdgen.sh /motdgen.sh

RUN apt update &&\
    apt -y upgrade &&\
    apt -y install cowsay cookietool fortune-anarchism fortune-mod fortunes fortunes-bofh-excuses fortunes-off fortunes-spam lolcat &&\
    rm -rf /var/lib/apt/lists/* &&\
    apt-get clean &&\
    chmod +x /motdgen.sh

CMD "/motdgen.sh"