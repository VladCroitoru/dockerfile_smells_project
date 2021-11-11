FROM centos:8

RUN yum -y install epel-release && \
    yum -y install ansible-2.9.7 which net-tools bind-utils iputils tree jq unzip git && \
    yum clean all && \
    rm -rf /var/cache/yum && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    rm -rf awscliv2.zip && \
    ./aws/install && \
    /usr/local/bin/aws --version

RUN mkdir /root/.aws && \
    mkdir /root/bin
ADD files/login_iam.sh /root/bin/
ADD files/assume_role.sh /root/bin/
ADD files/gds-apex-devops-role.sh /root/bin/
ADD files/.bash_profile /root/.bash_profile
RUN source /root/.bash_profile

#    pip3 install awscli --upgrade
#    yum -y install python-argcomplete ansible && \
#    yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools python2-pip && \
#    yum -y install git vim wget tree openssh-client jq traceroute openvpn unzip && \
#    yum -y install net-tools bind-utils && \

# ADD docker/files/requirements.txt .
# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt

#RUN echo -e '[local]\nlocalhost' > /etc/ansible/hosts

# RUN useradd ansible && \
#     mkdir /home/ansible/.ssh && \
#     chown ansible:ansible /home/ansible/.ssh

# WORKDIR /tmp/ansible
# ADD docker/files/VERSION .

ENV ANSIBLE_VERSION 2.9.7
ENV TZ=Asia/Singapore


# tail is running in the foreground to keep container running
CMD ["tail", "-f", "/dev/null"]
