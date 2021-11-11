#Run OpenStack Ocata Keystone in a container. Uses default configuration initialized with admin:admin:admin and enpoints pointing to localhost
FROM python:2-alpine
RUN apk update && apk add git build-base openssl-dev libffi-dev linux-headers
WORKDIR /usr/local/src/
RUN git clone -b stable/ocata  https://git.openstack.org/openstack/keystone.git
#Keystone and Oslo have conflicting version requirements for pbr and Babel. Giving priority to Oslo seems work 
RUN sed -i '/Babel/d /pbr/d' /usr/local/src/keystone/requirements.txt && pip install /usr/local/src/keystone/
RUN pip install uwsgi python-openstackclient
RUN apk del git build-base openssl-dev linux-headers
RUN mkdir -p /etc/keystone/fernet-keys
RUN cp /usr/local/src/keystone/etc/keystone-paste.ini /etc/keystone && cp /usr/local/src/keystone/etc/keystone.conf.sample /etc/keystone/keystone.conf && cp /usr/local/src/keystone/etc/policy.json /etc/keystone/
RUN keystone-manage fernet_setup --keystone-user root --keystone-group root
#The following creates the db file in WORKDIR (/usr/local/src/)
RUN keystone-manage db_sync && keystone-manage bootstrap --bootstrap-password password --bootstrap-username admin --bootstrap-project-name admin --bootstrap-role-name admin --bootstrap-service-name keystone --bootstrap-region-id RegionOne --bootstrap-admin-url http://localhost:35357 --bootstrap-public-url http://localhost:5000 --bootstrap-internal-url http://localhost:5000
EXPOSE 5000 35357
CMD uwsgi --http localhost:35357 --wsgi-file /usr/local/bin/keystone-wsgi-admin & uwsgi --http localhost:5000 --wsgi-file /usr/local/bin/keystone-wsgi-public
