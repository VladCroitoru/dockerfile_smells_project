FROM osrf/ros:kinetic-desktop-full
# nvidia-docker hooks
LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV PATH /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}
RUN bash -c "source /opt/ros/$ROS_DISTRO/setup.bash &&\
	mkdir -p /catkin_ws/src && cd /catkin_ws/src && \
	git clone https://github.com/davvdg/rviz-cam-widget.git &&\
	cd /catkin_ws &&\
	catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/$ROS_DISTRO-local install &&\
	cd / && rm -rf catkin_ws"
RUN sed -i s/\\/setup/\-local\\/setup/g ros_entrypoint.sh