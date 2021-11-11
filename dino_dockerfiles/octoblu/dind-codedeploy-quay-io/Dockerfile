FROM octoblu/builder
MAINTAINER serveradmin@octoblu.com

RUN apt-get update && apt-get install -y python-pip groff jq && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install awscli

ADD wait_and_codedeploy.sh /

CMD ["./wait_and_codedeploy.sh"]
