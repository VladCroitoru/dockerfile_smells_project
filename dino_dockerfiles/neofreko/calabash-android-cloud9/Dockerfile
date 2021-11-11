FROM codenvy/android442

RUN sudo apt-get update && \
sudo apt-get install -y -q build-essential curl git ruby zlib1g-dev libssl-dev \
libreadline-dev libyaml-dev libxml2-dev libxslt-dev ruby-dev libffi-dev

RUN git clone https://github.com/sstephenson/rbenv.git /home/user/.rbenv
RUN git clone https://github.com/sstephenson/ruby-build.git /home/user/.rbenv/plugins/ruby-build
RUN sudo /home/user/.rbenv/plugins/ruby-build/install.sh
ENV PATH /home/user/.rbenv/bin:$PATH
USER root
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile

USER user
RUN echo 'PATH=/home/user/.rbenv/bin:$PATH' >> .bashrc
RUN echo 'eval "$(rbenv init -)"' >> .bashrc
RUN rbenv install 1.9.3-p551

RUN rbenv global 1.9.3-p551 && \
eval "$(rbenv init -)" && \
rbenv shell 1.9.3-p551 && \
rbenv exec gem install bundler && \
rbenv rehash

# adb
RUN adb kill-server && chmod a+rw -R /home/user/android-sdk-linux/ && \
 echo "y" | android update sdk -u -a -t "platform-tool,build-tools-23.0.1,tools"

# update mesa, emulator requires GLX 1.3
RUN sudo apt-get install -y -q libgl1-mesa-swx11

RUN echo 'PATH=~/android-sdk-linux/platform-tools/:~/android-sdk-linux/tools/:$PATH' >> ~/.bashrc

# copypaste for vnc
RUN mkdir .vnc && touch .vnc/xstartup && echo 'autocutsel -s PRIMARY -fork' > .vnc/xstartup

# install cloud9
RUN git config --global url."https://".insteadOf git:// && \
git clone git://github.com/c9/core.git c9sdk &&\
cd c9sdk &&\
scripts/install-sdk.sh

# Tweak standlone.js conf
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /home/user/c9sdk/configs/standalone.js

RUN echo 'C9_DIR=$HOME/.c9' >> .bashrc
RUN echo 'PATH=$C9_DIR/node/bin:$PATH' >> .bashrc

ADD conf/cloud9.conf /opt/cloud9.conf
USER root
RUN cat /opt/cloud9.conf >> /opt/supervisord.conf

RUN sed -i -e 's_command=/opt/noVNC/utils/launch.sh_command=/opt/noVNC/utils/launch.sh --vnc 0.0.0.0:5900_' /opt/supervisord.conf

USER user

#manymo
RUN curl https://raw.githubusercontent.com/manymo/manymo/master/manymo-installer | bash

VOLUME /workspace
#ADD $app$ /home/user/application.apk

EXPOSE 8080
