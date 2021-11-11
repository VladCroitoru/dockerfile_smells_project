#RUN apt-get update
#Installation de postfix
#RUN apt-get install postfix
#RUN sudo apt-get install ;
#Image postfix, system: UBUNTU
FROM catatnight/postfix:latest
#**************************
#Création des utilisateurs*
#**************************
#RUN groupadd vmail -g 5000
#RUN useradd vmail -r -c 'virtual mail user' -m -d /home/vmail -g vmail -u 5000
#--------------------------
#RUN echo mail.wt18.ephec-ti.be > /etc/mailname
#RUN echo vmail: vmail@wt18.ephec-ti.be >> /etc/aliases
#COPY postfix_conf/ /etc/postfix
#RUN apt-get update && apt-get install dovecot-core dovecot-imapd -y
#COPY /dovecot_conf /etc/dovecot
#RUN touch /var/log/dovecot-deliver.log
#RUN chmod o+rw /var/log/dovecot-deliver.log
#RUN newaliases
#RUN postmap /etc/postfix/virtual
#RUN /etc/init.d/postfix restart
#RUN dovecot
