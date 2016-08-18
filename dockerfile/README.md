## Readme

0x00 ### install docker

`
sudo apt-get install docker-engine
`

0x01 ### install docker-compose

`
curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
`

0x02 ### build docker images

`
cd /path/
docker-compose build
`

0x03 ### run docker image

`
cd /path/
docker-compose up
`

0x04 ### check docker container status

`
docker-compose ps
`

0x05 ### check in http

`
http://localhost:8000/api
`
