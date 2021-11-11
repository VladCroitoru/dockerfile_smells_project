FROM centos:7
MAINTAINER "Jeff Geiger" <@jeffgeiger>

USER root
RUN curl https://copr.fedorainfracloud.org/coprs/g/rocknsm/rocknsm-2.1/repo/epel-7/group_rocknsm-rocknsm-2.1-epel-7.repo -o /etc/yum.repos.d/rocknsm-2.1-epel-7.repo && \
  yum install epel-release -y && \
  yum makecache fast && \
  yum install fsf yara python2-yara jq -y && \
  ln -f -s /opt/fsf/fsf-server/main.py /usr/local/bin/ && \
  ln -f -s /opt/fsf/fsf-client/fsf_client.py /usr/local/bin/ && \
  yum clean all && \
  rm -rf /var/cache/yum/* && \
  sed -i "s/\/FULL\/PATH\/TO\/fsf\/fsf-server\/yara/\/var\/lib\/yara-rules/" /opt/fsf/fsf-server/conf/config.py && \
  sed -i 's/socket.gethostname()/"127.0.0.1"/' /opt/fsf/fsf-server/conf/config.py && \
  groupadd -r nonroot && \
  useradd -r -g nonroot -d /home/nonroot -s /sbin/nologin -c "Nonroot User" nonroot && \
  mkdir /home/nonroot && \
  mkdir -pv /home/nonroot/workdir && \
  chown -R nonroot:nonroot /home/nonroot && \
  rm -rf /var/cache/yum/*

USER nonroot
ENV HOME /home/nonroot
ENV USER nonroot
WORKDIR /home/nonroot/workdir

ENTRYPOINT main.py start && printf "\n\n" && echo "<----->" && echo "FSF server daemonized!" &&  echo "<----->" && printf "\n" && echo "Invoke fsf_client.py by giving it a file as an argument:" && printf "\n" && echo "fsf_client.py <file>"  && printf "\n" && echo "Alternatively, Invoke fsf_client.py by giving it a file as an argument and pass to jq so you can interact extensively with the JSON output:" && printf "\n" && echo "fsf_client.py <file> | jq - C . | less -r" && printf "\n" && echo "To access all of the subobjects that are recursively processed, simply add --full when invoking fsf_client.py:" && printf "\n" && echo "fsf_client.py <file> --full" && printf "\n" && /bin/bash
