FROM ipoddaribm/powerai-examples

ADD ./NAE/help.html /etc/NAE/help.html
#WORKDIR /opt/DL
#RUN wget https://s3.amazonaws.com/yb-lab-cfg/Tensorflow-Tutorials.tar.gz; tar xvf Tensorflow-Tutorials.tar.gz; rm Tensorflow-Tutorials.tar.gz


#WORKDIR /root
#ADD startjupyter.sh /root/.startjupyter.sh 
#ADD startjupyter_py3.sh /root/.startjupyter_py3.sh
#ADD startdigits.sh  /root/.startdigits.sh
#ADD starttensorboard.sh /root/.starttensorboard.sh 
#ADD starttftuts.sh /root/.starttftuts.sh
ADD yb-sw-config.NIMBIX.ppc64le.mdt100.sh /root/sw-config.sh

#RUN chmod +x /root/.startjupyter.sh \
#&& chmod +x /root/.startjupyter_py3.sh \
#&& chmod +x /root/.startdigits.sh \
#&& chmod +x /root/.starttensorboard.sh \
#&& chmod +x /root/.starttftuts.sh \
RUN chmod +x /root/sw-config.sh

#ADD conf.d/* /etc/supervisor/conf.d/

#ADD ./install.tar /usr/local

#COPY ./.bashrc /etc/skel/.bashrc

#add NIMBIX application
COPY AppDef.json /etc/NAE/AppDef.json
RUN curl --fail -X POST -d @/etc/NAE/AppDef.json https://api.jarvice.com/jarvice/validate

#RUN pip install -U scikit-learn \
#&& pip install -U prettytensor

#COPY ./jupyterhub_config.py /usr/local/jupyterhub_config.py

#RUN rm /root/startdigits.sh \
#&& rm /root/starttensorboard.sh \
#&& rm /root/startjupyter.sh

WORKDIR /home/nimbix
RUN /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/ibm-6.9.1.0-node-v6.9.1-linux-ppc64le.bin \
&& /usr/bin/wget  https://s3.amazonaws.com/yb-lab-cfg/admin/yb-admin.NIMBIX.ppc64le.tar \

&& tar xvf yb-admin.NIMBIX.ppc64le.tar -C /usr/bin \
&& sudo apt-get install -y tcl \
&& sudo apt-get install -y git \

&& echo 'export PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH' >> .bashrc \
&& echo 'export PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH' >> /etc/bash.bashrc \
&& export PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH \

&& sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config \

&& sudo apt-get install -y python-h5py python-scipy cmake \
&& git clone https://github.com/sunqm/pyscf \
&& cd pyscf/lib \
&& mkdir build 
#&& cd build \
#&& cmake .. 
#&& make







