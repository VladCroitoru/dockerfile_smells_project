FROM circleci/node:8-browsers

RUN google-chrome --version

RUN curl "https://install.meteor.com/?release=1.8" | /bin/sh
RUN echo "Meteor version:";meteor --version;which meteor;echo "Meteor node version:";meteor node -v;echo "Meteor npm version:";meteor npm -v;echo "Java version:";java -version
RUN meteor npm install --global yarn
RUN meteor npm install --global chimpy@classcraft/chimpy#babel_7_dist

USER root
RUN git clone https://www.agwa.name/git/git-crypt.git
RUN cd git-crypt && make && make install

USER circleci
