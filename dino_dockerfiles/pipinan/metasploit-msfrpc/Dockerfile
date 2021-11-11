FROM kalilinux/kali-linux-docker

RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list && \
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean

#https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers
RUN apt-get install -y curl apt-utils nmap python ruby ruby-dev postgresql 
RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
	chmod 755 msfinstall && \
	./msfinstall
	
RUN service postgresql start  && msfconsole
#RUN gem update && gem install msgpack

EXPOSE 5432
EXPOSE 55553
CMD msfrpcd -P 123456 -n -f -a 0.0.0.0