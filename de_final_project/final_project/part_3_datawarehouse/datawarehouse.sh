#!/bin/bash

# launch postgres shell
psql --username=postgres --host=localhost

# list current DBs
\l

# create database
create database staging

# connect to staging
\c staging

# create schema using SQL from create_schema.sql