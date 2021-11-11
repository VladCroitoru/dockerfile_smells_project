FROM ipoddaribm/powerai-examples

ADD ./NAE/help.html /etc/NAE/help.html
#WORKDIR /opt/DL
#RUN wget https://s3.amazonaws.com/yb-lab-cfg/Tensorflow-Tutorials.tar.gz; tar xvf Tensorflow-Tutorials.tar.gz; rm Tensorflow-Tutorials.tar.gz


WORKDIR /root

ADD startjupyter.sh /root/.startjupyter.sh 
ADD startjupyter_py3.sh /root/.startjupyter_py3.sh
ADD startdigits.sh  /root/.startdigits.sh
ADD starttensorboard.sh /root/.starttensorboard.sh 
ADD starttftuts.sh /root/.starttftuts.sh
ADD jpy_nb_start.sh /root/.jpy_nb_start.sh
ADD yb-sw-config.NIMBIX.ppc64le.p8AI.sh /root/sw-config.sh

RUN chmod +x /root/.startjupyter.sh \
&& chmod +x /root/.startjupyter_py3.sh \
&& chmod +x /root/.startdigits.sh \
&& chmod +x /root/.starttensorboard.sh \
&& chmod +x /root/.starttftuts.sh \
&& chmod +x /root/.jpy_nb_start.sh \
&& chmod +x /root/sw-config.sh 

ADD conf.d/* /etc/supervisor/conf.d/

COPY ./.bashrc /etc/skel/.bashrc
COPY ./jupyterhub_config.py /usr/local/jupyterhub_config.py

#add NIMBIX application
COPY AppDef.json /etc/NAE/AppDef.json
RUN curl --fail -X POST -d @/etc/NAE/AppDef.json https://api.jarvice.com/jarvice/validate \

&& /root/sw-config.sh \
&& rm /root/sw-config.sh \
&& echo 'export PATH=/root/anaconda3/envs/tensorflow/bin:$PATH' >> /root/.bashrc \
&& echo 'export PYTHONPATH=/root/anaconda3/envs/tensorflow/lib/python3.6:/root/anaconda3/envs/tensorflow/lib/python3.6/site-packages/:/root/anaconda3/envs/tensorflow/lib/python3.6/site-packages/prettytensor-0.7.2-py3.6.egg:/root/anaconda3/envs/tensorflow/lib/python3.6/site-packages/enum34-1.1.6-py3.6.egg:/root/anaconda3/envs/tensorflow/lib/python3.6/site-packages/setuptools-27.2.0-py3.6.egg:/root/anaconda3/envs/tensorflow/lib/python3.6/site-packages/matplotlib:$PYTHONPATH' >> /root/.bashrc \

&& /usr/bin/wget https://github.com/google/prettytensor/archive/master.zip -P /root \
&& unzip master.zip \
&& rm master.zip \
&& cd prettytensor-master \
&& /root/anaconda3/envs/tensorflow/bin/python setup.py install \
&& /root/anaconda3/envs/tensorflow/bin/pip install gym \
&& /root/anaconda3/envs/tensorflow/bin/pip install atari_py \
&& /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/Tensorflow-Tutorials.tar.gz -P /opt/DL \
&& tar xvf /opt/DL/Tensorflow-Tutorials.tar.gz -C /opt/DL \
&& /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/Tensorflow-101.tar.gz -P /opt/DL \
&& tar xvf /opt/DL/Tensorflow-101.tar.gz -C /opt/DL \
&& /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/basics.tar.gz -P /opt/DL \
&& tar xvf /opt/DL/basics.tar.gz -C /opt/DL \
&& /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/ExplorePyComp.tar.gz -P /opt/DL \
&& tar xvf /opt/DL/ExplorePyComp.tar.gz -C /opt/DL \
&& /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/LearnDataScience.tar.gz -P /opt/DL \
&& tar xvf /opt/DL/LearnDataScience.tar.gz -C /opt/DL \
&& /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/DeepLearningKerasTensorflow.tar.gz -P /opt/DL \
&& tar xvf /opt/DL/DeepLearningKerasTensorflow.tar.gz -C /opt/DL \


&& apt-get install -y gfortran \
&& apt-get update \

&&  /root/anaconda3/envs/tensorflow/bin/pip install numpy scipy \
&&  /root/anaconda3/envs/tensorflow/bin/pip install scikit-learn \
&&  /root/anaconda3/envs/tensorflow/bin/pip install pillow \
&&  /root/anaconda3/envs/tensorflow/bin/conda install h5py \
&&  /root/anaconda3/envs/tensorflow/bin/pip install keras \
&&  /root/anaconda3/envs/tensorflow/bin/pip install gensim \

&& rm /opt/DL/Tensorflow-Tutorials.tar.gz \
&& rm /opt/DL/Tensorflow-101.tar.gz \
&& rm /opt/DL/basics.tar.gz \
&& rm /opt/DL/ExplorePyComp.tar.gz \
&& rm /opt/DL/LearnDataScience.tar.gz \
&& rm /opt/DL/DeepLearningKerasTensorflow.tar.gz \
&& rm /root/Anaconda3-4.4.0-Linux-ppc64le.sh \
&& rm -rf /root/prettytensor-master 




WORKDIR /home/nimbix
RUN /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/ibm-6.9.1.0-node-v6.9.1-linux-ppc64le.bin \
&& /usr/bin/wget  https://s3.amazonaws.com/yb-lab-cfg/admin/yb-admin.NIMBIX.ppc64le.tar \

&& tar xvf yb-admin.NIMBIX.ppc64le.tar -C /usr/bin \
&& sudo apt-get install -y tcl \
&& sudo apt-get install -y git 


#&& echo 'export PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH' >> .bashrc \
#&& echo 'export PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH' >> /etc/bash.bashrc \
#&& export PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH \

#&& sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config \
#&& sudo service ssh restart 

#&& /root/.starttftuts.sh 9002 
#&& /usr/bin/yb-jpytokens






