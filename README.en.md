*Ler em [Português](README.md)*

# Docker Toy Application

Application made with python to test docker funcionalities, the idea is to have different containers communicating info. Two containers will simulate sensors creating random values of temperature and humidity, both publishing their values in rabbitmq container. Another container will be subscribed to rabbitmq and will save the publications. A user application can request publications on an given id, that is generated together with every value the sensors publish.

## Usage

Its possible to test the application by just running ```bash docker-compose up ``` in the root folder. Or initialize every docker container by the docker file in each folder. After starting the containers, the root folder has a user.py archive, which is the applicationused to consult values by the id. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.