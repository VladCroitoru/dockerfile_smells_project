FROM library/ubuntu:16.04
MAINTAINER Schwannden Kuo<schwannden@gmail.com>

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 
ENV SBT_HOME=/usr/share/sbt/bin/
ENV PATH $JAVA_HOME/bin:$SBT_HOME/bin:$PATH
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update \
    && apt-get install -y git vim wget curl tree htop apt-transport-https unzip curl tmux iputils-ping locales \
    && locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8\
    && apt-get install -y zsh \
    && git clone --depth 1 https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
    && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
    && echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 \
    && apt-get update && apt-get install -y sbt default-jdk \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \
    && echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.2.list \
    && apt-get update && apt-get install -y mongodb-org \
    && chsh -s /bin/zsh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY .vimrc /root/.vimrc
COPY .zshrc /root/.zshrc

CMD ["zsh"]
