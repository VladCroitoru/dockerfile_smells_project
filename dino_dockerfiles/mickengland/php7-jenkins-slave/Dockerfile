FROM jenkinsci/jnlp-slave 
USER root
RUN echo "deb http://http.us.debian.org/debian/ testing non-free contrib main" >> /etc/apt/sources.list
RUN apt-get update 
RUN  apt-get install -y apt-utils
RUN  apt-get install -y build-essential
RUN apt-get install -t testing -y php7.0 
RUN apt-get install -t testing -y php7.0-gmp 
RUN apt-get install -t testing -y php7.0-soap
USER jenkins
