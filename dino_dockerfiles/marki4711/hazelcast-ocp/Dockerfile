FROM hazelcast/openshift:3.7.5 
  
USER root 
  
# Move Hazelcast Config File to subfolder, to allow replacement with ConfigMap machanism 
RUN mkdir ${HZ_HOME}config \ 
 && mv ${HZ_HOME}hazelcast.xml ${HZ_HOME}config/ \ 
 && ln -s ${HZ_HOME}config/hazelcast.xml ${HZ_HOME}hazelcast.xml 

RUN useradd -r hazelcast 

USER hazelcast 
  
# Start hazelcast standalone server. 
CMD ./start.sh 
