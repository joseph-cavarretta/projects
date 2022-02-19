'''
1. Setup connection to weather API
2. Decide what features to include
    - Best practice for time series analysis
    - Best practice for weather modelling
        - Daily high temp vs daily mean temp
        - Daily low temp
        - Daily(?) mean wind speed vs peak wind speed
        - Daily rainfall
3. Pull data
4. EDA
    - Structure/clean data (what to consider here?)
    - Time series EDA best practices
        - Min/Max Scaler
    - Non-categorical so no encoding needed?
    - Boulder, CO
5. Specific Anomaly Detection model seletion
    - Manual using 3 SDs on univariates
    - Isolation Forest
    - Classification? Logistic Regression? Anomaly or not?
    - What hyperparameters are there?
    - Do I need to split data, how to do so with time series?
6. Build model
7. Test and validate model
'''
