# eq_robot_mqtt_broker
Example of creating an MQTT server with publisher in ROS Noetic and python subscriber

## Prerequisites
You must have 
1. Docker
1. Docker-compose

## Run the example
Clone the repository and navigate to the root folder
```shell
sudo -E docker-compose up
```
Note that the `-E` option is what enables passing environment variables from the host machine to the container.
   
If you wish to force re-building of the docker images
```shell
sudo -E docker-compose up --build
```
The docker-compose should now spin up three containers.
1. mqtt_broker
    - The MQTT server which relays messages. This is based on [VerneMQ](https://github.com/vernemq/vernemq).
1. mqtt_publisher
    - A ROS Noetic network spinning up a publisher which publishes dummy data to the broker at 1 Hz. The communication 
    on the ROS network is relayed to the MQTT broker through an [mqtt_bridge](https://github.com/groove-x/mqtt_bridge).
1. mqtt_subscriber
    - Subscriber written in Python which uses the [paho mqtt client](https://github.com/eclipse/paho.mqtt.python).
    
The publisher will print its published message while the subscriber will echo the message. 

### VerneMQ status interface
The VerneMQ status interface is exposed in localhost and may be accessed at 
```shell
http://localhost:8888/status
```

## Accessing the containers
Each container may be accessed after startup through the following command
```shell
sudo docker exec -it <container_name> /bin/bash
```

## Administering the MQTT Broker
### User management
Note that the example currently has anonymous access enabled by default!

A user exists with the following credentials for the sake of the example
- Username: test_user
- Password: test_password

To manage the user/password file see the official VerneMQ [documentation](https://docs.vernemq.com/configuration/file-auth).

### Broker inspection
To inspect the broker during runtime you may use `docker exec` to access the container and use the `vmq-admin` tool to
inspect the broker. See the VerneMq [documentation](https://docs.vernemq.com/administration/introduction) for more details.

## Credits
Thanks to [The EIT-hub experiments](https://github.com/equinor/eit-hub-experiments) repository for heplful guide to 
VerneMQ.
