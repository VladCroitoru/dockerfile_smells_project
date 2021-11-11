FROM centos:6.6
MAINTAINER Eugene Petrenko <Eugene.Petrenko@jetbrains.com>

ENV GIT_VERSION 2.8.4
ADD install_git.sh git.sh /root/

RUN ["/bin/bash", "-c", "chmod a+x /root/install_git.sh && sync && /root/install_git.sh $GIT_VERSION && rm -rf /root/install_git.sh && mv /root/git.sh /git && sync && chmod a+rx /git"]

CMD /bin/bash -c "cat /git; echo \"# See /git-.*.sh for git versions. Use the script to run it\""

