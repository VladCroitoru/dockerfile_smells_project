FROM eivantsov/jdk8
RUN mkdir /home/user/maven3 && \
    wget -qO- "http://archive.apache.org/dist/maven/maven-3/3.1.1/binaries/apache-maven-3.1.1-bin.tar.gz" | tar -zx --strip-components=1 -C /home/user/maven3
ENV M2_HOME /home/user/maven3   
RUN echo "export M2_HOME=$M2_HOME" >> /home/user/.bashrc
ENV PATH $M2_HOME/bin:$PATH
RUN echo "export PATH=$PATH" >> /home/user/.bashrc
RUN sudo apt-get update && sudo apt-get -y install git curl libdigest-sha-perl gcc python
RUN sudo apt-get -y install ruby-full build-essential ruby-compass
RUN echo 'export PATH=/home/user/local/bin:$PATH' >> /home/user/.bashrc
RUN mkdir /home/user/local
RUN mkdir /home/user/node-latest-install
RUN cd /home/user/node-latest-install && curl http://nodejs.org/dist/node-latest.tar.gz | tar xz --strip-components=1 && ./configure --prefix=/home/user/local && make install
RUN sudo apt-get -y install nodejs-legacy
RUN cd /home/user && wget https://www.npmjs.org/install.sh && sudo chmod a+x install.sh && sleep 1 && sudo ./install.sh
RUN mkdir /home/user/.nvm
RUN git clone https://github.com/creationix/nvm.git /home/user/.nvm
ENV NVM_DIR /home/user/.nvm
RUN echo "export NVM_DIR=/home/user/.nvm" >> /home/user/.bashrc
ENV PATH $NVM_DIR:$PATH
RUN echo "export PATH=$PATH" >> /home/user/.bashrc
RUN export NVM_DIR=/home/user/.nvm
ENV HOME /home/user/
RUN cd /home/user/.nvm && sudo chmod a+x install.sh && sleep 1 && ./install.sh && \
echo "[[ -s /home/user/.nvm/nvm.sh ]] && . /home/user/.nvm/nvm.sh" >> /home/user/.bashrc && . /home/user/.nvm/nvm.sh && \
      nvm install 4.2.1
RUN sudo npm install -g npm@2.14.7
RUN sudo npm install --global gulp@3.8.7
RUN sudo gem install jekyll -v 2.3.0
RUN mkdir /home/user/app
RUN rm -rf /home/user/maven3/conf/settings.xml
WORKDIR /home/user/app
