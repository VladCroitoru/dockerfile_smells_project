FROM debian:10

RUN apt-get update &&\
	apt-get install -y sudo git-core subversion mercurial build-essential libssl-dev libncurses5-dev unzip gawk wget python3 &&\
	apt-get clean -y &&\
	useradd -m lede &&\
	echo 'lede ALL=NOPASSWD: ALL' > /etc/sudoers.d/lede &&\
	sudo -iu lede git clone https://github.com/lede-project/source.git lede-project &&\
	sudo -iu lede lede-project/scripts/feeds update
