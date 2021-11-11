FROM unidata/python

#switch to root 
USER root
  
# add the scripts from github to the image 
COPY GABLS3-CFDWindSCM/ /home/jovyan/work/
COPY GABLS3DiurnalCycleBenchmarkForWindEnergy_2017.ipynb /home/jovyan/work/
RUN chown -R $NB_USER:users /home/jovyan/work/
COPY start.sh /usr/local/bin/windbench_start.sh
RUN chown -R $NB_USER:users /usr/local/bin/windbench_start.sh
RUN chmod +x /usr/local/bin/windbench_start.sh

# switch back to the standard user
USER jovyan

#create a directory for mounting data
RUN mkdir /home/$NB_USER/work/data

CMD ["windbench_start.sh"]
