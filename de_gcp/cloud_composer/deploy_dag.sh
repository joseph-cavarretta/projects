gcloud composer environments storage dags \
import --environment <cloud composer environment name> \
--location <cloud composer region> \
--source <dag-file.py>

# check dags
# <cloud composer gcs bucket>/dags/