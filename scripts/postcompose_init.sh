#!/bin/bash

# dev
mongo --host $(docker-machine ip dev):27017 admin scripts/user_init.js --quiet

mongo --host $(docker-machine ip dev):27017 devdb scripts/mongo_init.js --quiet

# prod

#mongo --host $(docker-machine ip volta):27017 admin scripts/user_init.js --quiet

#mongo --host $(docker-machine ip volta):27017 codeboxsystems scripts/mongo_init.js --quiet
