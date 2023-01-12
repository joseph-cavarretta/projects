from google.cloud import bigquery
from google.cloud.exceptions import NotFound

client = bigquery.Client()
dataset_names = ['raw_activities','processed_activities']
location = 'US'

def create_bigquery_dataset(dataset_name):
    """Create bigquery dataset. Check first if the dataset exists
    Args:
        dataset_name: string
    """
    dataset_id = f"{client.project}.{dataset_name}"
    try:
        client.get_dataset(dataset_id)
        print(f"Dataset {dataset_id} already exists")
    except NotFound:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location
        dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
        print(f"Created dataset {client.project}.{dataset.dataset_id}")


for name in dataset_names:
    create_bigquery_dataset(name)
