## Sample web app that generates HTTP traffic randomly

Starts three flask web servers listening on ports defined in set-env-vars.sh
Starts a background container that will randomly make requests to each web server every 20 to 40 seconds.

Can easily be modified or extended, replace flask with a socket server, add more servers, etc

Meant to be run on a server and expects to be able to hit each web server by external IP, so probably won't work when running locally.

### Dependencies

Docker
Docker compose
envsubst

### Instructions

```bash
./start.sh
```
