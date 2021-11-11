FROM smattis/rmswuq-docker
MAINTAINER Steve Mattis

# Install BET
RUN cd $HOME/src && \
    rm -r -f BET && \
    mkdir tmp && \
    cd tmp && \
    git clone https://github.com/UT-CHG/BET.git 
   
   
#RUN chmod -R a+rwx $HOME

# Add Demos
RUN cd $HOME/demos && \
    cp -R ../src/tmp/BET/examples BET-examples && \
    git clone https://smattis@bitbucket.org/vcarey/rm-workshop.git && \
    mv rm-workshop error-estimation-demos && \
    chmod -R a+rwx $HOME/demos 

ADD WELCOME /home/rmswuq/WELCOME