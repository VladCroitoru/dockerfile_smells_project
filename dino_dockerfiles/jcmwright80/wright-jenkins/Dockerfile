FROM jenkins
# if we want to install via apt
USER root
RUN apt-get update && apt-get install -y ruby && su -c "gem install sass"
USER jenkins
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
