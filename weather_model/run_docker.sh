#!/bin/bash
docker run \
--rm \
--it
--volume ~/*/weather_model/src/data:/data \
weather_model