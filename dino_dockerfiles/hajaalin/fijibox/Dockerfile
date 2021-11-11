FROM hajaalin/devbox

# set up SSH access for 'dev'
RUN apt-get install -y openssh-server \
&& mkdir /var/run/sshd \
&& echo 'dev:123'|chpasswd

EXPOSE 22

# install Fiji: have to figure out how to manage new versions...
RUN cd / \
&& wget http://jenkins.imagej.net/job/Stable-Fiji/lastSuccessfulBuild/artifact/fiji-linux64.tar.gz \
&& tar xf fiji-linux64.tar.gz \
&& rm fiji-linux64.tar.gz \
&& Fiji.app/ImageJ-linux64 --update update-force-pristine \
&& cd Fiji.app/plugins \
&& wget http://rsb.info.nih.gov/ij/plugins/download/jars/Image_Moments.jar \ 
&& chown -R dev: /Fiji.app

ADD fiji.sh /etc/profile.d/fiji.sh
RUN chmod 0555 /etc/profile.d/fiji.sh

CMD ["/usr/sbin/sshd", "-D"] 




