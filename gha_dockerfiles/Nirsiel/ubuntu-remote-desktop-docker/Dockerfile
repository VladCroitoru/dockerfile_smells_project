FROM dorowu/ubuntu-desktop-lxde-vnc:latest

#Switching sources.list for clean 20.04 one.
RUN sudo mv /etc/apt/sources.list /etc/apt/sources.list.old
COPY sources.list /etc/apt/sources.list

#Removing build-in browsers
RUN sudo dpkg --remove google-chrome-stable && sudo apt-get -y autoremove

#Updating and installing basic tools
RUN sudo apt-get update -y && sudo apt-get upgrade -y
RUN sudo apt-get install -y software-properties-common apt-transport-https build-essential gdebi-core unzip wget curl htop ncdu zip atop vim ssh git 

#Install VSCode
RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
RUN sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
RUN sudo apt-get update -y && sudo apt-get install -y code=1.56.2-1620838498

#Install Pale Moon browser (https://www.palemoon.org/)
RUN sudo echo 'deb http://download.opensuse.org/repositories/home:/stevenpusser/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:stevenpusser.list
RUN sudo curl -fsSL https://download.opensuse.org/repositories/home:stevenpusser/xUbuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_stevenpusser.gpg > /dev/null
RUN sudo apt-get update -y && sudo apt-get install -y palemoon

#Install Alacritty
RUN sudo add-apt-repository ppa:aslatter/ppa
RUN sudo apt-get install -y alacritty

#Install PeaZip (https://peazip.github.io/)
RUN wget https://github.com/peazip/PeaZip/releases/download/8.2.0/peazip_8.2.0.LINUX.GTK2-1_amd64.deb
RUN sudo gdebi -n peazip_8.2.0.LINUX.GTK2-1_amd64.deb
RUN sudo rm -f peazip_8.2.0.LINUX.GTK2-1_amd64.deb

#Install AnyDesk (anydesk.com)
RUN wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -
RUN sudo echo "deb http://deb.anydesk.com/ all main" > /etc/apt/sources.list.d/anydesk-stable.list
RUN sudo apt-get update && sudo apt-get install -y anydesk

#Removing Apt cache
RUN rm -rf /var/lib/apt/lists/*