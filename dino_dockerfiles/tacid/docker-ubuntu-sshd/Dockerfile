FROM ubuntu:xenial

RUN apt update && apt install -y --no-install-recommends \
        vim \
        ssh \
        wget \
        curl \
        command-not-found \
        iputils-ping \
        bind9-host \
        ca-certificates \
        fakeroot \
        git \
        rake \
        sudo \
        bash-completion \
        apt-transport-https \
        locales \
    && rm -rf /var/lib/apt/lists/*

RUN curl -L https://bit.ly/janus-bootstrap | bash && mkdir -p /root/.vim/colors

RUN echo '"\e[A":  history-search-backward	# Previous' >> /etc/inputrc \
    && echo '"\e[B":  history-search-forward		# Next' >> /etc/inputrc

COPY vimrc_after /root/.vimrc.after
COPY codeschool.vim /root/.vim/colors/
COPY bashrc /root/.bashrc
COPY gitconfig /root/.gitconfig

RUN locale-gen ru_RU.UTF-8 en_US.UTF-8 && update-locale

RUN mkdir -p /root/.ssh/ \
    && mkdir /var/run/sshd \
    && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWIXR7c7w0F1xe3RdU6MO3zDln9UhCvcdJcC2EJX3jCyrmWgjA2UNYIznK7SRoOXMDEMkGAhzEbeIu4BHWs+pio9Gd9OJcXr9X3pXXUJoeRr5ddL6juOOUvIc4k76jjWB2Uy4h5zuqCw/4XrNJnMmMRJA/tGSpDsqZbQt9ZHWEFjBp+gsvNNmEtsNna05ZquQi3seQ39fiykPRHlP6ZXX8Z0HIHmQhMI4xuB6tuDLzFbNqr4giHlZxNb7Ak3rhGyk6u7midxvsZ8AIE50rkpqqC5HDIyWs9j7HKfI5idRylaemS/Mk2hA/wa50Edsq3V/OiegYXV9AyqnLx9x7ENGx srvadm@srvadm-Lenovo-G50-70" >> /root/.ssh/authorized_keys

EXPOSE 22

CMD /usr/sbin/sshd -D
