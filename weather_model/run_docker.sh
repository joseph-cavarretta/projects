#!/bin/bash

docker run \
--rm \
--volume ~/*/weather_model/src/data:/data \
weather_model