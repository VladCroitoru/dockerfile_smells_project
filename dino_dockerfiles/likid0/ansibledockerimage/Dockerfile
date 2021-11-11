from ubuntu:trusty

# Install Ansible
RUN apt-get update -qy && \
    apt-get install -qy software-properties-common && \
    apt-add-repository -y ppa:ansible/ansible && \
    apt-get update -qy && \
    apt-get install -qy ansible

# Copy baked in playbooks
COPY probe-service.yml /ansible/

# Add volume for Ansible playbooks
VOLUME /ansible
WORKDIR /ansible

# Entrypoint
ENTRYPOINT ["ansible-playbook"]
CMD ["probe-service.yml"]           
