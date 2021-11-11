# This Dockerfile is used to build an image containing basic stuff to be used as a Jenkins slave build node. based on evarga/jenkins-slave
FROM stevenhorsman/jenkins-slave

# Install pax
RUN apt-get update && apt-get install -y \
pax \
&& rm -rf /var/lib/apt/lists/*

CMD ["/usr/sbin/sshd", "-D"]
