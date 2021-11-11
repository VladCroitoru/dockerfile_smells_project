FROM node:4.3.2

RUN apt-get update && apt-get install -y sqlite3 awscli curl unzip git vim less && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/hirenj/aws-runbuild /aws-runbuild
RUN chmod +x /aws-runbuild/run_buildstep.sh

COPY setup_build.sh /aws-runbuild/setup_build.sh

CMD ["/bin/bash","/aws-runbuild/setup_build.sh"]