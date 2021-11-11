FROM jenkins/jenkins:2.286
USER root
RUN apt-get update && apt-get install -y rsync nano python && rm -rf /var/lib/apt/lists/*
RUN groupadd -g 412 docker && gpasswd -a jenkins docker
RUN mkdir -p /opt/git-subrepo && git clone https://github.com/ingydotnet/git-subrepo /opt/git-subrepo && echo 'source /opt/git-subrepo/.rc' >> /var/jenkins_home/.bashrc
USER jenkins
