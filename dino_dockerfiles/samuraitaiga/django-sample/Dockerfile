FROM     centos
MAINTAINER TAIGA "samuraitaiga@gmail.com"

# make sure the package repository is up to date

# prepare ansible
RUN yum clean all
RUN yum install -y python python-devel python-setuptools wget git gcc
RUN git clone -b v1.8.2 https://github.com/ansible/ansible.git /opt/ansible; cd /opt/ansible; git submodule update --init --recursive; python setup.py install

# checkout repository which has ansible playbook
RUN git clone https://github.com/samuraitaiga/django-sample.git /opt/django-sample
RUN cd /opt/django-sample; echo "127.0.0.1" > hosts; ansible-playbook playbook.yml --connection=local -i hosts

EXPOSE 8000
CMD    ["python", "/opt/django-sample/djangosample/manage.py", "runserver", "0.0.0.0:8000"]
