FROM scazlab/human_robot_collaboration:master

RUN cd ~/ros_ws/src \
    && git clone https://github.com/scazlab/baxter_tictactoe.git
RUN cd ~/ros_ws/src \
    && wstool merge -y baxter_tictactoe/dependencies.rosinstall
# wstool st is because of some git bug (!) https://github.com/vcstools/wstool/issues/77
RUN cd ~/ros_ws/src \
    && wstool st && wstool up

USER root
RUN  cd ~/ros_ws \
     && rosdep install -y --from-paths src --ignore-src --rosdistro $ROS_DISTRO
USER ros
RUN  cd ~/ros_ws && catkin build

CMD ["/bin/bash"]
