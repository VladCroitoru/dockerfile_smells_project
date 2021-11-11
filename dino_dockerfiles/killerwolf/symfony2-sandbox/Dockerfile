FROM ansible/ubuntu14.04-ansible
#FROM itech/ansible

MAINTAINER killerwolf

ADD ansible/ /tmp/ansible
ADD application/ /var/www/symfony2-sandbox

RUN ansible-playbook -i /etc/ansible/hosts --connection=local /tmp/ansible/playbook.local.yml
RUN ansible-playbook -i /etc/ansible/hosts --connection=local /tmp/ansible/playbook.yml

RUN /etc/init.d/mysql start 
RUN /etc/init.d/php5-fpm start 

EXPOSE 80
EXPOSE 3306

CMD ["nginx", "-g", "daemon off;"]