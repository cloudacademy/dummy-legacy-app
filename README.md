## Sample web app that generates HTTP traffic randomly

Starts three flask web servers listening on ports defined in set-env-vars.sh

Starts a background container that will randomly make requests to each web server every 10 to 40 seconds.

Can easily be modified or extended, replace flask with a socket server, add more servers, etc

Meant to be run on a server and expects to be able to hit each web server by external IP, so probably won't work when running locally.

### Dependencies

- Docker
- Docker compose
- envsubst
- bash

### Instructions

```bash
./start.sh
```

### Using in EC2 User Data

#### Download, Extract, and Start

```bash
echo --- installing and starting dummy legacy app ---
# Master as an example, consider using a release, branch or tag
ZIP_URL="https://github.com/cloudacademy/dummy-legacy-app/archive/master.zip"
cd /tmp && wget "$ZIP_URL" && unzip master.zip && cd dummy-legacy-app-master && ./start.sh && cd ~
```
