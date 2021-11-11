FROM ferag/barridocker:latest

RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-add-repository ppa:ansible/ansible
RUN apt-get update && \
    apt-get install -y ansible && \
    rm -rf /var/lib/apt/lists/* 
RUN ansible-galaxy install indigo-dc.oneclient && \
    ansible-playbook /etc/ansible/roles/indigo-dc.oneclient/tests/test.yml
