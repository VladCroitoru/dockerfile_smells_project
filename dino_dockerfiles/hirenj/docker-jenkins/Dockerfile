FROM jenkins:latest

USER root
RUN apt-get update && apt-get install -y sudo git supervisor && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://get.docker.com/ | sh

# Make sure jenkins user has docker privileges
RUN usermod -aG docker jenkins

USER jenkins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

USER root

# Create log folder for supervisor and jenkins
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /var/log/jenkins

# Copy the supervisor.conf file into Docker
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

# Start supervisord when running the container
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf