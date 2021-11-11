FROM ubuntu

RUN apt-get update
RUN apt-get -y install wget vim ttf-ancient-fonts git
WORKDIR /home
RUN wget https://github.com/emojicode/emojicode/releases/download/v0.2.0-beta.5/Emojicode-0.2.0-beta.5-x86_64-linux-gnu.tar.gz
RUN tar -zxvf Emojicode-0.2.0-beta.5-x86_64-linux-gnu.tar.gz
WORKDIR Emojicode-0.2.0-beta.5-x86_64-linux-gnu
RUN git clone https://github.com/emojicode/emojicode sourcefile
ENV TERM xterm
RUN ./install.sh
