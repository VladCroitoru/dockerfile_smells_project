FROM node:0.12.0
MAINTAINER Vincent Elcrin <vincent.elcrin@gmail.com>

RUN apt-get update && apt-get install -y build-essential zsh

# Install Zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
    && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

# Zsh plugins (git, node, npm, mvn, docker, bower)
# plugins=(git, node, npm, mvn, docker, bower)
RUN sed -i 's/ZSH_THEME=.*/ZSH_THEME="candy"/g' ~/.zshrc
RUN sed -i 's/plugins=.*/plugins=(git,node,npm,mvn,docker,bower)/g' ~/.zshrc

# Install Java
RUN apt-get install -y openjdk-7-jre
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/

# Install Maven
RUN apt-get install -y maven

WORKDIR /workspace
CMD ["/bin/zsh"]
EXPOSE 3000 35729
