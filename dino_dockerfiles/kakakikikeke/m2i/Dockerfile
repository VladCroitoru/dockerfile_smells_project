FROM perl:5.34.0

ARG md="example.md"

# Mount a markdownfile
ADD . /root

# Install nginx
RUN apt -y update
RUN apt -y install nginx
RUN apt -y install fonts-vlgothic fonts-takao-gothic fonts-ipafont-gothic fonts-ipaexfont-gothic

# Install libs
RUN cpanm Data::Section::Simple
RUN cpanm Text::Markdown
RUN cpanm Text::Xslate
RUN cpanm Path::Class

# Install markdown2imporess
WORKDIR /root
RUN git clone https://github.com/yoshiki/markdown2impress.git

# Generate resources
WORKDIR /root/markdown2impress/bin/
RUN ./markdown2impress.pl /root/${md}
RUN cp -ipr index.html js/ css/ /var/www/html/

# Start Slide
EXPOSE 80
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]