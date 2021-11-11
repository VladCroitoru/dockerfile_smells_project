FROM maven:3.2-jdk-7
RUN apt-get update
RUN apt-get install build-essential bison openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libxml2-dev autoconf libc6-dev ncurses-dev automake libtool -y
RUN apt-get install rubygems -y
RUN apt-get install ruby-dev -y
RUN gem install github_changelog_generator
RUN wget https://github.com/justrelease/justrelease/releases/download/v1.1.5/justrelease-core-1.1.5.zip
RUN unzip justrelease-core-1.1.5.zip
WORKDIR justrelease-core-1.1.5
CMD java -jar justrelease-1.1.5.jar $arg
