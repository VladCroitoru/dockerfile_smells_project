#Fichier docker d'installation du serveur

#effacer toutes les images : docker rmi $(docker images -a -q)
#effacer tous les containers : docker rm  $(docker ps -a -f status=exited -q)


#install docker :
#sudo curl -sSL get.docker.com | sh
#systemctl start docker
#systemctl enable --now docker
#configurer le firewall via cockpit aver ouverture des port pour mongoDB & 6800
#pour fedora 31 : https://linuxconfig.org/how-to-install-docker-on-fedora-31
#dnf install -y grubby && grubby --update-kernel=ALL --args="systemd.unified_cgroup_hierarchy=0" && reboot

#renouvellement des certificats
#désactiver le parefeu puis
#certbot certonly --standalone --email hhoareau@gmail.com -d server.f80.fr
#cp /etc/letsencrypt/live/server.f80.fr/* /root/certs

#fabrication: docker build -t f80hub/elmoney . & docker push f80hub/elmoney:latest
#installation: docker rm -f elmoney && docker pull f80hub/elmoney:latest
#démarrage prod : docker rm -f elmoney && docker pull f80hub/elmoney && docker run --restart=always -v /root/certs:/certs -p 5555:5555 --name elmoney -d f80hub/elmoney:latest python3 app.py 5555 devnet tokenforge ssl

#Ouverture des ports : firewall-cmd --zone=public --add-port=7777/tcp
#fabrication: docker build -t f80hub/elmoney-dev . & docker push f80hub/elmoney-dev:latest
#démarrage test : docker rm -f elmoney-dev && docker pull f80hub/elmoney-dev && docker run --restart=always -v /root/certs:/certs -p 7777:7777 --name elmoney-dev -d f80hub/elmoney-dev:latest python3 app.py 7777 testnet coinmaker ssl


FROM python:3.9.0-buster



# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 -v install Flask
RUN pip3 -v install Flask-Cors
RUN pip3 -v install pyyaml

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install pynacl
RUN pip3 install pycryptodome

RUN export PATH="$HOME/.local/bin:$PATH"
RUN pip3 install --user --upgrade --no-cache-dir erdpy==1.0.19
RUN pip3 install pyopenssl

RUN pip3 -v install apscheduler
RUN pip3 -v install pymongo
RUN pip3 -v install flask-socketio==4.3.2
RUN pip3 -v install aes-everywhere
RUN pip3 -v install flask-excel
RUN pip3 -v install pandas
RUN pip3 -v install ipfshttpclient
RUN pip3 -v install Flask-Caching
RUN pip3 -v install requests-cache
RUN pip3 -v install multiaddr
#RUN pip3 -v install py7zr



WORKDIR /
RUN mkdir PEM
RUN mkdir temp
RUN mkdir static
VOLUME /certs

COPY *.py $APP_HOME/
COPY ./static $APP_HOME/static
COPY ./PEM $APP_HOME/PEM


#CMD ["python3", "app.py","5555","http://161.97.75.165:7590","coinmaker-test","ssl"]
CMD ["python3", "app.py","5555","https://testnet-api.elrond.com","coinmaker","ssl"]
