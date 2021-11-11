#
# This project should create a docker based on oidcfed-swamid-federation
# Please check your docker confirguration before run. 
# Ex. to run this project: 
#    docker run -t -d -p 8080:8080 -p 8100:8100 -p 8089:8089 tehnari/oidcfed-swamid-federation-docker:0.0.1 /bin/bash
# For local build see ex. below:
# docker build --rm -t tehnari/oidcfed-swamid-federation-docker:0.0.1 .
#
FROM opensuse/leap
LABEL Author="Constantin Sclifos sclifcon@ase.md"
LABEL Name=tehnari/oidcfed-swamid-federation-docker Version=0.0.1
EXPOSE 8080 8100 8089

WORKDIR /app
ADD . /app

RUN zypper -v ref && zypper -n in -l vim  nano git curl wget python3 python3-pip screen net-tools net-tools-deprecated && \
    whereis pip3

RUN python3 -m pip install --upgrade pip

COPY ./cleanup-oidc-swamid-federation.sh /app/cleanup-oidc-swamid-federation.sh
#COPY ./setup-oidc-swamid-federation.sh /app/setup-oidc-swamid-federation.sh   # Disabled, not working at this moment. Have some depency issue.
COPY ./setup-oidc-swamid-federation-v2.sh /app/setup-oidc-swamid-federation-v2.sh
RUN chmod 777 /app/*.sh
RUN cd /app 

#RUN screen -A -m -d -S bash /app/setup-oidc-swamid-federation.sh &
#CMD ["nohup", "/app/setup-oidc-swamid-federation.sh > /app/setup-output.txt 2>&1 &"] 
#ENTRYPOINT nohup /app/setup-oidc-swamid-federation.sh  > /app/setup-output.txt 2>&1 &
#CMD nohup /app/setup-oidc-swamid-federation.sh  > /app/setup-output.txt 2>&1 & && bash
#ENTRYPOINT ["nohup", "/app/setup-oidc-swamid-federation.sh > /app/setup-output.txt 2>&1 &"] 
#CMD ["-c"]

#RUN chmod +x ./entrypoint.sh
#CMD [ "/bin/bash" , "./entrypoint.sh"] 
#echo "Sleep for 60 seconds..." && sleep 60s && \
# echo "All operations should be finished. If not launch manually setup-oidc-swamid-federation.sh." && \
# echo "And don't forget before to start cleanup ;) "
#RUN ss -tulpn | grep 80
#RUN netstat -tulpnv | grep 80
