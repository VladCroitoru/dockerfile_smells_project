#FROM debian:wheezy
FROM ubuntu:14.04
MAINTAINER Jose Miguel de la Casa <nacicansao@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN echo "root:temporal" | chpasswd
ADD sources.list /etc/apt/sources.list
#RUN echo "deb http://http.debian.net/debian wheezy main contrib non-free" > /etc/apt/sources.list
#RUN echo "deb http://http.debian.net/debian wheezy-updates main contrib non-free" >> /etc/apt/sources.list
#RUN echo "deb http://security.debian.org wheezy/updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "Acquire::http::Proxy \"http://192.168.112.7:3128\";" > /etc/apt/apt.conf



# install ssh and supervisord
RUN apt-get update
RUN apt-get install -y --force-yes curl ssh supervisor apt-utils
RUN mkdir /var/run/sshd
RUN chown root:root /var/run/sshd
RUN mkdir /var/log/supervisord

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
#RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' /etc/pam.d/sshd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login                        
# RUN sed 's@session\s*required\s*pam_loginuid.so@session optional  pam_loginuid.so@g' -i /etc/pam.d/sshd
# ENV NOTVISIBLE "in users profile"                                                                                                                
# RUN echo "export VISIBLE=now" >> /etc/profile 

RUN apt-get -y --force-yes install git  python-pip gcc  build-essential python-dev wget tcpdump vim
RUN apt-get -y --force-yes install virtualbox
RUN mkdir /home/workspace

# install cuckoo
RUN cd /home/workspace/ ; git clone git://github.com/cuckoobox/cuckoo.git       
RUN pip install -r /home/workspace/cuckoo/requirements.txt                      
RUN useradd cuckoo                                                              
RUN usermod -a -G vboxusers cuckoo # add cuckoo to vboxusers group              
ADD start_cuckoo.sh /home/workspace/start_cuckoo.sh
ADD start_cuckoo_web.sh /home/workspace/start_cuckoo_web.sh
ADD virtualbox.conf /home/workspace/cuckoo/conf/virtualbox.conf    

RUN apt-get -y --force-yes install python-magic # for identifying file formats              
RUN apt-get -y --force-yes  install python-dpkt # for extracting info from pcaps             
RUN apt-get -y --force-yes install python-mako # for rendering html reports and web gui     
RUN apt-get -y --force-yes install python-sqlalchemy                                        
RUN apt-get -y --force-yes install python-jinja2 # necessary for web.py utility             
RUN apt-get -y --force-yes install python-bottle # necessary for web.py utility   

#RUN apt-get -y install ssdeep                                                   
RUN apt-get -y --force-yes install python-pyrex # required for pyssdeep installation        
RUN apt-get -y --force-yes install subversion                                               
#RUN apt-get -y install libfuzzy-dev  

RUN apt-get -y --force-yes install python-pymongo # for mongodb support  
RUN apt-get -y --force-yes install mongodb # includes server and clients 

RUN apt-get -y --force-yes install libcap2-bin  
#RUN setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump  
#RUN  getcap /usr/sbin/tcpdump # to check changes have been applied 
EXPOSE 22 9001 

#ENTRYPOINT
CMD ["/usr/bin/supervisord"]


