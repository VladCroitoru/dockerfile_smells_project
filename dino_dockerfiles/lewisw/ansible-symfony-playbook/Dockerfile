FROM lewisw/ansible-symfony-playbook
MAINTAINER Lewis Wright <lewis@allwrightythen.com>

# Create the structure
WORKDIR /project

COPY github-oauth.token github-oauth.token
RUN /composer_oauth github-oauth.token

# Copy the role requirements and run them
COPY ansible/install-dependencies.sh ansible/install-dependencies.sh
COPY ansible/requirements.yml ansible/requirements.yml
RUN /ansible_dependencies

# Copy any files used in provisioning & provision
COPY ansible ansible
COPY app/config/parameters.yml.dist app/config/parameters.yml.dist
RUN /apt_cacher leeroy.vivait.co.uk; /ansible_setup && /graceful_shutdown

# Copy any composer files and pre-download them
COPY composer.json composer.lock ./
RUN echo "${IP} leeroy.vivait.co.uk" >> /etc/hosts; /composer_setup

# Try and provision, so we can atleast cache
COPY ./ ./
RUN echo "${IP} leeroy.vivait.co.uk" >> /etc/hosts; /ansible_update && /graceful_shutdown
