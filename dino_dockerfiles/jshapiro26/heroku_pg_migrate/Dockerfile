FROM centos:7

WORKDIR /opt/

# Add postgres repo
RUN rpm -iUvh http://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm

# Install a basic SSH server GIT, UNZIP, LSOF, JDK 8, apache maven, redis and nodejs
RUN yum update -y
RUN yum install -y postgresql96 postgresql96-server postgresql96-contrib postgresql96-libs postgresql-devel \
  which \
  sudo \
  wget
RUN yum clean all

# Disable tty or sudo wont work 
RUN sed -i "s/requiretty/!requiretty/g" /etc/sudoers

# Install RVM
RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN sudo \curl -sSL https://get.rvm.io | bash -s stable --ruby

# Install default rvm versions. 
RUN /usr/local/rvm/bin/rvm install 2.3.1

# Install Heroku toolbelt
RUN sudo wget -qO- https://toolbelt.heroku.com/install.sh | sh 
RUN echo 'PATH="/usr/local/heroku/bin:$PATH"' >> ~/.profile

# Modify postgres
ADD utf8.sql utf8.sql
ADD modify_pg.sh modify_pg.sh
RUN chmod +x /opt/modify_pg.sh
RUN /opt/modify_pg.sh

# Copy entry script
COPY entry.sh /bin/entry.sh
RUN chmod +x /bin/entry.sh

# Remove existing pg_dump and symlink to 9.6 binary
RUN rm -rf /usr/bin/pg_dump
RUN ln -s /usr/pgsql-9.6/bin/pg_dump /usr/bin/pg_dump

ENTRYPOINT ["entry.sh"]