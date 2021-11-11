FROM dammeax/xpspark
RUN yum -y install gcc python-devel; yum clean all
RUN pip install --upgrade matplotlib seaborn
RUN curl -s http://wwwftp.ciril.fr/pub/apache/zeppelin/zeppelin-0.7.3/zeppelin-0.7.3-bin-all.tgz | tar xz -C /opt
RUN ln -s /opt/zeppelin-0.7.3-bin-all /opt/zeppelin
WORKDIR /opt/zeppelin-0.7.3-bin-all
RUN cp conf/shiro.ini.template conf/shiro.ini
RUN sed -i 's/admin = password1/xp = vlab4xp/' conf/shiro.ini
RUN sed -i 's/user1 = password2, role1, role2//' conf/shiro.ini
RUN sed -i 's/user2 = password3, role3//' conf/shiro.ini
RUN sed -i 's/user3 = password4, role2//' conf/shiro.ini
RUN cp conf/zeppelin-site.xml.template conf/zeppelin-site.xml
RUN sed -i '/<name>zeppelin.anonymous.allowed<\/name>/{n;s/<value>.*<\/value>/<value>false<\/value>/;}' conf/zeppelin-site.xml
