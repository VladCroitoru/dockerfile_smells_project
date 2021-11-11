# CentOS7 + ssh + ttyjs (in Supervisord)
FROM centos:centos7
RUN \
  yum update -y && \
  yum install -y epel-release && \
  yum install -y net-tools python-setuptools hostname inotify-tools yum-utils coreutils pwgen && \
  yum clean all

# Install supervisord
RUN  easy_install supervisor

# Prepare the container for our use with a Volume for logs and apps (/data)
# Prepare the container for our use with a directory to run custom bootstrap procedure
RUN mkdir -p /config/init && \
    mkdir -p /data

# Environment variable provision to accept root-password while creating container
ENV ROOT_PASS password

# Create /etc/supervisord.conf
RUN echo "[supervisord]" > /etc/supervisord.conf && \
    echo "pidfile = /run/supervisord.pid" >> /etc/supervisord.conf && \
    echo "# It seems that it's not possible to swith this log to NONE (it creates NONE logfile)" >> /etc/supervisord.conf && \
    echo "logfile = /data/logs/supervisord.log" >> /etc/supervisord.conf && \
    echo "# Set loglevel=debug, only then all logs from child services are printed out" >> /etc/supervisord.conf && \
    echo "# to container logs (and thus available via the command below - " >> /etc/supervisord.conf && \
    echo "#             docker logs [container]" >> /etc/supervisord.conf && \
    echo "loglevel = debug" >> /etc/supervisord.conf && \
    echo "" >> /etc/supervisord.conf && \
    echo "# These two (unix_http_server, rpcinterface) are needed for supervisorctl to work" >> /etc/supervisord.conf && \
    echo "[inet_http_server]" >> /etc/supervisord.conf && \
    echo "port = :9111" >> /etc/supervisord.conf && \
    echo "username = sv" >> /etc/supervisord.conf && \
    echo "password = password" >> /etc/supervisord.conf && \
    echo "" >> /etc/supervisord.conf && \
    echo "[rpcinterface:supervisor]" >> /etc/supervisord.conf && \
    echo "supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface" >> /etc/supervisord.conf && \
    echo "" >> /etc/supervisord.conf && \
    echo "[supervisorctl]" >> /etc/supervisord.conf && \
    echo "serverurl = http://localhost:9111" >> /etc/supervisord.conf && \
    echo "username = sv" >> /etc/supervisord.conf && \
    echo "password = password" >> /etc/supervisord.conf && \
    echo "" >> /etc/supervisord.conf && \
    echo "[include]" >> /etc/supervisord.conf && \
    echo "files = /etc/supervisor.d/*.conf" >> /etc/supervisord.conf

# Create /config/bootstrap.sh
RUN printf '%s\n' "#!/bin/bash" > /config/bootstrap.sh && \
    printf '%s\n' "" >> /config/bootstrap.sh && \
    printf '%s\n' "set -e" >> /config/bootstrap.sh && \
    printf '%s\n' "set -u" >> /config/bootstrap.sh && \
    printf '%s\n' "" >> /config/bootstrap.sh && \
    printf '%s\n' "# Supervisord default params" >> /config/bootstrap.sh && \
    printf '%s\n' "SUPERVISOR_PARAMS='-c /etc/supervisord.conf'" >> /config/bootstrap.sh && \
    printf '%s\n' "" >> /config/bootstrap.sh && \
    printf '%s\n' "" >> /config/bootstrap.sh && \
    printf '%s\n' "# Create directories for supervisor's UNIX socket and logs (which might be missing" >> /config/bootstrap.sh && \
    printf '%s\n' "# as container might start with /data mounted from another data-container)." >> /config/bootstrap.sh && \
    printf '%s\n' "mkdir -p /data/conf /data/run /data/logs" >> /config/bootstrap.sh && \
    printf '%s\n' "chmod 711 /data/conf /data/run /data/logs" >> /config/bootstrap.sh && \
    printf '%s\n' " " >> /config/bootstrap.sh && \
    printf '%s\n' "if [ \"\$(ls /config/init/)\" ]" >> /config/bootstrap.sh && \
    printf '%s\n' "then" >> /config/bootstrap.sh && \
    printf '%s\n' "  for init in /config/init/*.sh; do" >> /config/bootstrap.sh && \
    printf '%s\n' "    . \$init" >> /config/bootstrap.sh && \
    printf '%s\n' "  done" >> /config/bootstrap.sh && \
    printf '%s\n' "fi" >> /config/bootstrap.sh && \
    printf '%s\n' "" >> /config/bootstrap.sh && \
    printf '%s\n' "" >> /config/bootstrap.sh && \
    printf '%s\n' "# We have TTY, so probably an interactive container..." >> /config/bootstrap.sh && \
    printf '%s\n' "if test -t 0; then" >> /config/bootstrap.sh && \
    printf '%s\n' "  # Run supervisord detached..." >> /config/bootstrap.sh && \
    printf '%s\n' "  supervisord \$SUPERVISOR_PARAMS" >> /config/bootstrap.sh && \
    printf '%s\n' "" >> /config/bootstrap.sh && \
    printf '%s\n' "  # Some command(s) has been passed to container? Execute them and exit." >> /config/bootstrap.sh && \
    printf '%s\n' "  # No commands provided? Run bash." >> /config/bootstrap.sh && \
    printf '%s\n' "  if [[ \$@ ]]; then " >> /config/bootstrap.sh && \
    printf '%s\n' "    eval \$@" >> /config/bootstrap.sh && \
    printf '%s\n' "  else " >> /config/bootstrap.sh && \
    printf '%s\n' "    export PS1='[\\u@\\h : \\w]\\\$ '" >> /config/bootstrap.sh && \
    printf '%s\n' "    /bin/bash" >> /config/bootstrap.sh && \
    printf '%s\n' "  fi" >> /config/bootstrap.sh && \
    printf '%s\n' "" >> /config/bootstrap.sh && \
    printf '%s\n' "# Detached mode? Run supervisord in foreground, which will stay until container is stopped." >> /config/bootstrap.sh && \
    printf '%s\n' "else" >> /config/bootstrap.sh && \
    printf '%s\n' "  # If some extra params were passed, execute them before." >> /config/bootstrap.sh && \
    printf '%s\n' "  # @TODO It is a bit confusing that the passed command runs *before* supervisord, " >> /config/bootstrap.sh && \
    printf '%s\n' "  #       while in interactive mode they run *after* supervisor." >> /config/bootstrap.sh && \
    printf '%s\n' "  #       Not sure about that, but maybe when any command is passed to container," >> /config/bootstrap.sh && \
    printf '%s\n' "  #       it should be executed *always* after supervisord? And when the command ends," >> /config/bootstrap.sh && \
    printf '%s\n' "  #       container exits as well." >> /config/bootstrap.sh && \
    printf '%s\n' "  if [[ \$@ ]]; then " >> /config/bootstrap.sh && \
    printf '%s\n' "    eval \$@" >> /config/bootstrap.sh && \
    printf '%s\n' "  fi" >> /config/bootstrap.sh && \
    printf '%s\n' "  supervisord -n \$SUPERVISOR_PARAMS" >> /config/bootstrap.sh && \
    printf '%s\n' "fi" >> /config/bootstrap.sh && \
    chmod +x /config/bootstrap.sh

# Install openssh-server
RUN \
    yum install --nogpgcheck -y openssh-server openssh-clients pwgen sudo hostname wget patch htop iftop vim mc links && \
    yum clean all && \
    sed -i 's/UsePAM\syes/UsePAM no/' /etc/ssh/sshd_config && \
    ssh-keygen -q -b 1024 -N '' -t rsa -f /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -b 1024 -N '' -t dsa -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -q -b 521 -N '' -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key && \
    sed -i -r 's/.?UseDNS\syes/UseDNS no/' /etc/ssh/sshd_config && \
    sed -i -r 's/.?ChallengeResponseAuthentication.+/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config && \
    sed -i -r 's/.?PermitRootLogin.+/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create supervisord config file for sshd
RUN mkdir /etc/supervisor.d
RUN echo "[program:sshd]" > /etc/supervisor.d/sshd.conf && \
	echo "command=/usr/sbin/sshd -D" >> /etc/supervisor.d/sshd.conf && \
	echo "stdout_logfile=/data/logs/sshd.log" >> /etc/supervisor.d/sshd.conf && \
	echo "stderr_logfile=/data/logs/sshd.log" >> /etc/supervisor.d/sshd.conf

# Create custom configuration file for setting root-password
RUN printf '%s\n' "#!/bin/bash" > /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "set -e" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "set -u" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "export TERM=xterm" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "# Bash Colors" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "red=\`tput setaf 1\`" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "green=\`tput setaf 2\`" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "yellow=\`tput setaf 3\`" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "white=\`tput setaf 7\`" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "bold=\`tput bold\`" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "reset=\`tput sgr0\`" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "separator=\$(echo && printf '=%.0s' {1..100} && echo)" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "# Logging Function" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "log() {" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "  if [[ \"\$@\" ]]" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "  then" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "     echo \"\${bold}\${green}[SSHD `date +'%T'`]\${reset} \$@\";" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "  else" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "      echo" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "  fi" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "}" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "# Generate password for root" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "if [ \${ROOT_PASS} == password ]" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "then" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "   ROOT_PASS=\$(pwgen -c -n -1 16)" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "fi" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "echo \"root:\${ROOT_PASS}\" | chpasswd" >> /config/init/10-init-set-root-pass.sh && \
    printf '%s\n' "log \"root password set to: \${white}\${bold}\$ROOT_PASS\${reset}\"" >> /config/init/10-init-set-root-pass.sh && \
    chmod +x /config/init/10-init-set-root-pass.sh

# Install Nodejs and other dependencies for tty.js
RUN yum -y install make
RUN yum -y install npm
RUN yum -y install nodejs
RUN npm install -g express
RUN npm install -g socket.io
RUN npm install -g tty.js
RUN ssh-keygen -A

# Create supervisord config file for tty.js
RUN echo "[program:node]" >> /etc/supervisor.d/tty.js.conf && \
    echo "command=/usr/bin/tty.js" >> /etc/supervisor.d/tty.js.conf &&\
    echo "stdout_logfile=/data/logs/tty.js.log" >> /etc/supervisor.d/tty.js.conf && \
    echo "stderr_logfile=/data/logs/tty.js.log" >> /etc/supervisor.d/tty.js.conf

# Expose sshd and tty.js ports
EXPOSE 22 8080

# Bootstrap the container with root-password while supervisord launches sshd & tty.js
ENTRYPOINT ["/config/bootstrap.sh"]
