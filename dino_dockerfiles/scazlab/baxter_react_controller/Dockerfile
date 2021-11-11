FROM scazlab/hrc-docker:baxter

# Compile IPOPT first
USER root
RUN apt-get -y install wget gfortran libgfortran-4.9-dev
USER ros

ENV IPOPT_DIR  /home/ros/src/ipopt/build
RUN mkdir ~/src && cd ~/src \
    && svn co --trust-server-cert --non-interactive https://projects.coin-or.org/svn/Ipopt/stable/3.12 ipopt
RUN mkdir $IPOPT_DIR \
    && cd $IPOPT_DIR/../ThirdParty \
    && cd ASL    && ./get.ASL    && cd ../ \
    && cd Blas   && ./get.Blas   && cd ../ \
    && cd Lapack && ./get.Lapack && cd ../ \
    && cd Metis  && ./get.Metis  && cd ../ \
    && cd Mumps  && ./get.Mumps  && cd ../
RUN cd $IPOPT_DIR \
    && ../configure && make -j8
USER root
RUN cd $IPOPT_DIR \
    && sudo make install
USER ros

# Compile the repo afterwards
RUN cd ~/ros_ws/src \
    && git clone https://github.com/scazlab/baxter_react_controller.git  \
    && wstool merge -y  baxter_react_controller/dependencies.rosinstall \
    && wstool up

USER root
RUN  cd ~/ros_ws \
     && rosdep install -y --from-paths src --ignore-src --rosdistro $ROS_DISTRO
USER ros
RUN  cd ~/ros_ws && catkin build

CMD ["/bin/bash"]
