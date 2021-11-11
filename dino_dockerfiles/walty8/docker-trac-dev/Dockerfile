FROM ubuntu:14.04


USER root

WORKDIR /root

#Install basic environment
RUN apt-get -y update && \
    apt-get -y install \
        python-pip \
        git \
	subversion \ 
	python-subversion \
        openssh-server \
	supervisor \
	apache2-utils \
	vim



#Get the latest Trac code
#http://trac.edgewall.org/wiki/TracDev/DevelopmentEnvironmentSetup
#I used git clone instead of svn co here
RUN git clone https://github.com/edgewall/trac trac-trunk 
RUN git clone https://github.com/edgewall/genshi genshi-trunk
RUN cd genshi-trunk && python setup.py develop 
RUN cd trac-trunk && python setup.py develop

#Set up test instance of Trac
RUN trac-admin test initenv TestTrac  sqlite:db/trac.db
RUN trac-admin test permission add anonymous TRAC_ADMIN 

#Set up authentication file
RUN htpasswd -bc test/passwd user1 pass1
RUN htpasswd -b test/passwd user2 pass2
RUN htpasswd -b test/passwd user3 pass3

#Set up Trac developer plugin
RUN svn co https://trac-hacks.org/svn/tracdeveloperplugin/trunk/ tracdeveloperplugin
RUN cd tracdeveloperplugin && python setup.py bdist_egg && cp dist/*.egg ../test/plugins


#Set up SSH access
RUN mkdir /var/run/sshd
RUN sed -i.bak s/PermitRootLogin\ without-password/PermitRootLogin\ yes/g  /etc/ssh/sshd_config
RUN echo "root:trac" | chpasswd

#Set Trac configuration
COPY resources/trac.ini /root/test/conf/trac.ini

#Set up SVN repository
RUN mkdir temp
RUN svnadmin create svn-repo
COPY resources/sample-project temp/svn-sample-project
COPY resources/post-commit /root/svn-repo/hooks/post-commit
RUN cd temp && svn import svn-sample-project file:///root/svn-repo/svn-sample-project -m "initial import of svn sameple project"
RUN svn co file:///root/svn-repo/svn-sample-project svn-sample-project
RUN cd svn-sample-project && echo 'bla bla bla' >> file1.txt
RUN cd svn-sample-project && svn commit -m "first change" --username=user1 


#Set up GIT repository
RUN mkdir git-repo
RUN git init --bare git-repo
COPY resources/post-receive /root/git-repo/hooks/post-receive
RUN chmod 755 /root/git-repo/hooks/post-receive
RUN git clone file:///root/git-repo git-sample-project
COPY resources/sample-project/ git-sample-project/
RUN git config --global user.email user2@example.com
RUN git config --global user.name user2
RUN git config --global push.default simple
RUN cd git-sample-project && git add file1.txt file2.txt
RUN cd git-sample-project && git commit -a -m "initial import" && git push
RUN cd git-sample-project && echo 'bla bla bla' >> file1.txt
RUN cd git-sample-project && git commit -a -m "first change" && git push


EXPOSE 8000 22

COPY resources/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY resources/restart_trac.sh /root/restart_trac.sh

CMD ["/usr/bin/supervisord"]
#CMD ["bash"]
