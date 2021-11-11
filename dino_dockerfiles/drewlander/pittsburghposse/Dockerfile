#
FROM fedora

RUN /bin/dnf install -yq deltarpm && \ 
 dnf install -y git \
		    ruby-2.4.1 \
                    rubygem-rake \
                    ruby-devel \
                    nginx \ 
		    libffi-devel \
		    gcc \
		    make \ 
		    rpm-build

#    dnf clean all
RUN /usr/bin/gem install rake &&  \
    /usr/bin/gem install bundle && \ 
   /usr/bin/gem install json

ENV HOME /home/user

RUN useradd  user -d $HOME \
	&& chown -R user $HOME

WORKDIR $HOME
RUN mkdir -p /usr/share/nginx/pittsburghposse
RUN /usr/bin/git clone  https://github.com/drewlander/pittsburghposse.git   /usr/share/nginx/pittsburghposse
RUN cd  /usr/share/nginx/pittsburghposse  && \
    bundle install && \
    jekyll build
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN mv  /usr/share/nginx/pittsburghposse/_site/* /usr/share/nginx/html
EXPOSE 80
EXPOSE 443
# Define default command.
CMD ["/usr/sbin/nginx"]

# Expose ports.

