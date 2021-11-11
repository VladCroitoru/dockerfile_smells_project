FROM kalilinux/kali-linux-docker:latest
RUN apt-get update && apt-get install -y git python-qt4-dev libqt4-qt3support
RUN mkdir /home/git/
WORKDIR /home/git
RUN git clone https://github.com/infobyte/faraday.git faraday
WORKDIR faraday
RUN ./install.sh
CMD /home/git/faraday/faraday.py
