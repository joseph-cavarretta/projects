#!/bin/bash

cd \
cd "\Program Files\MySQL\MySQL Server 8.0"

# make sure server is running
\bin\mysqld --console

# connect
mysql -u root -p