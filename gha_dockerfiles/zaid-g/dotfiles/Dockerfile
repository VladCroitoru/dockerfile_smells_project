#Download base image ubuntu 20.04
FROM ubuntu:20.04

# Update Ubuntu Software repository
RUN apt update
RUN apt-get update
RUN apt upgrade -y
RUN apt-get upgrade -y

RUN apt-get install git -y
RUN apt install zsh -y
RUN apt install python3 -y
RUN apt install vim -y
RUN apt install python3-pip -y

RUN pip3 install ipdb
RUN pip3 install pandas
RUN pip3 install black
RUN pip3 install flake8

RUN useradd -ms /usr/bin/zsh ubuntu
USER ubuntu
WORKDIR /home/ubuntu
RUN mkdir env
WORKDIR /home/ubuntu/env
RUN git clone https://github.com/zaid-g/dotfiles.git
WORKDIR /home/ubuntu/env/dotfiles
RUN . ./update.sh
WORKDIR /home/ubuntu/env/dotfiles
RUN . ./plugins-vim-install.sh
WORKDIR /home/ubuntu
RUN echo 'PS1="%B%{$fg[green]%}[%{$fg[green]%}%n%{$fg[green]%}@%{$fg[green]%}%M %{$fg[green]%}%~%{$fg[green]%}]%{$reset_color%}$%b "' >> .zshrc


ENTRYPOINT /usr/bin/zsh
