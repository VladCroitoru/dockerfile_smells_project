FROM fraoustin/gitweb
MAINTAINER fraoustin@gmail.com

RUN apt-get update && apt-get install -y \
        unzip \
        wget \
    && rm -rf /var/lib/apt/lists/* 


# file and parameter gitweb
RUN echo "\$feature{'highlight'}{'default'} = [1];" >> /etc/gitweb.conf

# change web
COPY ./src/ihm/static/* /usr/share/gitweb/static/
COPY ./src/ihm/*.html /usr/share/gitweb/
RUN cd /usr/share/gitweb/static && wget https://code.jquery.com/jquery-1.11.3.js
RUN cd /usr/share/gitweb/static && wget http://fontawesome.io/assets/font-awesome-4.7.0.zip && unzip font-awesome-4.7.0.zip && rm font-awesome-4.7.0.zip && mv font-awesome* font-awesome
RUN echo '$home_text="hometext.html";' >> /etc/gitweb.conf
RUN echo '$site_header="header.html";' >> /etc/gitweb.conf
RUN echo '$site_footer="footer.html";' >> /etc/gitweb.conf
RUN cat /usr/share/gitweb/headstring.html >> /etc/gitweb.conf

