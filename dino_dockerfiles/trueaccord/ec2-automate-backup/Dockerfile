FROM quay.io/trueaccord/miniubuntu:latest

RUN installpkg python2.7 git python-pip python-setuptools
RUN pip install awscli

RUN git clone https://github.com/colinbjohnson/aws-missing-tools.git /opt/aws-missing-tools

ENTRYPOINT ["/opt/aws-missing-tools/ec2-automate-backup/ec2-automate-backup.sh"]

