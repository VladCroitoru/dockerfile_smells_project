FROM centos
MAINTAINER Keenneeth Espinal keenneeth@mail.asix

RUN \
	#Actualitzar centos
	yum update -y && \
	#Instal·lar el repositori Epel
	yum install -y epel-release && \
	#Instal·lar eines de xarxa,navegador lynx  i dependencies de Supervisor
	yum install -y iproute python-setuptools hostname inotify-tools yum-utils which lynx && \
	#Netejar la memòria cau 
	yum clean all

	#Instal·lar Supervisor
RUN	easy_install supervisor

	#Instal·lar el Apache
RUN 	yum -y install httpd
RUN	systemctl enable httpd

	#Afegir fitxers de configuració
        ADD config /

	#Iniciar el minidlna al iniciar el contenidor
RUN	systemctl enable minidlnad

	#Variables d'entorn per crear usuari
	ENV USER=docker
	ENV PASSWORD=root

	#Exposar el port del Supervisor, http, minidlna
	EXPOSE 9001 80 8200

	#Comanda Sed per tal de canviar l'usuari creat de manera predeterminada, amb l'usuari que enviem amb les variables d'entorn 
RUN \
	sed -ri "s/docker/${USER}/g" /etc/supervisord.conf && \
	sed -ri "s/root/${PASSWORD}/g" /etc/supervisord.conf
	
	#Executar script del Supervisor
	ENTRYPOINT ["/config/bootstrap.sh"]
