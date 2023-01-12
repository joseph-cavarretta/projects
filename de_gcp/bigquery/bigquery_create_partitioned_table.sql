CREATE TABLE processed_activities (
    id INT64,
    start_date_local DATE,
    type STRING
)
PARTITION BY (start_date_local);