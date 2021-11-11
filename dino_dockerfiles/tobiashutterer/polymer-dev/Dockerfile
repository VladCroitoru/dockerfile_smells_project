FROM node:6.2.2
MAINTAINER Tobias Hutterer <github.com/tobiashutterer>
ENV NODE_ENV development
# defining a user because polymer-cli doesn't like root user!
ENV USER polymer
RUN apt-get update
RUN apt-get -y install sudo
# to skip password prompt for sudo users
RUN echo %sudo ALL=NOPASSWD: ALL >> /etc/sudoers
# setting up a user
RUN useradd --create-home --shell /bin/bash $USER && adduser $USER sudo
ENV HOME /home/$USER
WORKDIR $HOME
# making the $USER owner of node_modules dir to avoid permission errors
RUN chown -R $USER /usr/local/lib/node_modules/
RUN npm install -g bower grunt-cli gulp

# switching to the non-root user
USER $USER
RUN sudo npm install -g polymer-cli
RUN npm cache clear
EXPOSE 8080
CMD ["/bin/bash"]
