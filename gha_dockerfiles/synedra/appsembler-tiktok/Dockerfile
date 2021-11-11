FROM linuxserver/code-server

RUN apt-get update
RUN git clone https://github.com/synedra/appdev-week2-tiktok /config/workspace/tik-tok
ENV SUDO_PASSWORD=password
RUN apt-get install -y -q python3 python3-pip
RUN apt-get clean 
       
WORKDIR /config/workspace/tik-tok
RUN npm install netlify-cli astra-setup axios
RUN pip3 install httpie-astra

COPY /root /
EXPOSE 8443
