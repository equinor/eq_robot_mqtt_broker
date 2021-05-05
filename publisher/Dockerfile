FROM ros:noetic-ros-core
WORKDIR /home/
RUN \
    apt-get update

RUN \
    apt-get install -y \
    build-essential \
    python3-osrf-pycommon \
    python3-catkin-tools \
    python3-rosdep

RUN \
    mkdir -p catkin_ws/src


COPY ./ catkin_ws/src/publisher

WORKDIR /home/catkin_ws/

RUN \
    apt-get update &&\
    rosdep init &&\
    rosdep update &&\
    rosdep install --from-paths ./src --ignore-packages-from-source --rosdistro noetic -y

SHELL ["/bin/bash", "-c"]

RUN \
    source /opt/ros/noetic/setup.bash && \
    catkin build

RUN \
    source /opt/ros/noetic/setup.bash && \
    source devel/setup.bash

WORKDIR /home/catkin_ws/src/publisher
RUN \
    apt-get update && \
    apt-get install -y python3-pip && \
    pip3 --version

RUN \
    pip3 install -r requirements.txt

RUN chmod +x startup

EXPOSE 1883

ENTRYPOINT ./startup
CMD ["/bin/bash"]
