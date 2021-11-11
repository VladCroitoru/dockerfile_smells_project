# Build our documentation and push it to github 

FROM seqware/seqware_whitestar
MAINTAINER Denis Yuen <denis.yuen@oicr.on.ca>

USER seqware
WORKDIR /home/seqware

ADD config /home/seqware/.ssh/config
ADD private_key.pem /home/seqware/.ssh/id_rsa
RUN sudo chown -R seqware /home/seqware/.ssh ;\
    sudo chmod -R 600 /home/seqware/.ssh/* ;\
    eval "$(ssh-agent -s)" ;\
    ssh-add ~/.ssh/id_rsa ;\
    sudo apt-get -y install ruby1.9.3 ruby-rvm ruby-rdiscount ruby-nokogiri ;

# enforce US locale, seems to better agree with gems
USER root
RUN     sudo locale-gen en_US.UTF-8 ;\
	sudo dpkg-reconfigure locales ;\
        echo "export LANGUAGE=en_US.UTF-8" >> /etc/bash.bashrc ;\
	echo "export LANG=en_US.UTF-8" >> /etc/bash.bashrc ;\
	echo "export LC_ALL=en_US.UTF-8" >> /etc/bash.bashrc ;\
	echo "export LC_CTYPE=en_US.UTF-8" >> /etc/bash.bashrc ;\
	echo 'LANG="en_US.UTF-8"' | sudo tee /etc/default/locale ;\
	echo 'LC_ALL="en_US.UTF-8"' | sudo tee -a /etc/default/locale ;\
	echo 'LC_CTYPE="en_US.UTF-8"' | sudo tee -a /etc/default/locale ;\
	echo 'LANG="en_US.UTF-8"' | sudo tee -a /etc/environment ;\
	echo 'LC_ALL="en_US.UTF-8"' | sudo tee -a /etc/environment ;\
	echo 'LC_CTYPE="en_US.UTF-8"' | sudo tee -a /etc/environment

USER seqware
RUN     export LANGUAGE=en_US.UTF-8;\
        export LANG=en_US.UTF-8 ;\
	export LC_ALL=en_US.UTF-8 ;\
	export LC_CTYPE=en_US.UTF-8 ;\
        sudo gem install kramdown adsf mime-types compass haml coderay rubypants builder rainpress yajl-ruby pygments.rb ;\
        sudo gem install nanoc -v 3.7.1 ;\
        sudo gem uninstall yajl-ruby --version 1.2.1

RUN git config --global user.name "Seqware jenkins" ;\
    git config --global user.email seqware-jenkins@oicr.on.ca 

ADD settings.xml  /home/seqware/.m2/settings.xml
RUN sudo chown -R seqware /home/seqware/.m2/settings.xml
RUN git clone -b develop https://github.com/SeqWare/seqware.git 
WORKDIR /home/seqware/seqware
RUN mvn clean install -DskipTests 

# current gem version seems to fix the incompatibility
RUN sudo gem install yajl-ruby
