# possibly only works if bucket is already made?
export NEW_BUCKET_NAME=joe-test-bucket
export NEW_PATH=folder/other-folder
gsutil cp -r ./* gs://$NEW_BUCKET_NAME/$NEW_PATH