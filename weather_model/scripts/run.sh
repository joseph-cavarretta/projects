#!/bin/bash
docker run \
--rm \
--volume ~/projects/weather_model/src/data:/data \
--volume ~/projects/weather_model/src/data/scheduled_runs:/output \
-e GOOGLE_APPLICATION_CREDENTIALS=/run/user/1000/gvfs/google-drive:host=gmail.com,user=josephmc241/0AMIJ0BdVNPMaUk9PVA/10mVXLWqGBfgPcuY3qD_GbwLdcGyMhy8O/1tAbHoHj-y3-M_s8rRSXgbLmfBgxVZ2cE \
weather_model