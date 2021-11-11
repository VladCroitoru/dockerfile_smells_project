FROM gitlab/gitlab-ce:8.12.3-ce.0

RUN apt-get update && apt-get install -y openjdk-8-jre-headless subversion

RUN wget https://subgit.com/download/subgit_3.2.2_all.deb -O /opt/subgit_3.2.2_all.deb
RUN dpkg -i /opt/subgit_3.2.2_all.deb && rm /opt/subgit_3.2.2_all.deb

ADD custom-run.sh /usr/local/bin/

CMD ["/usr/local/bin/custom-run.sh"]

