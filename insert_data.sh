#!/bin/bash

if [ "$1" = "1" ]; then
    docker-compose run mssql-tools /opt/mssql-tools/bin/sqlcmd -S mssql -U SA -P Passw0rdOfs3cr3ts -i /data/1_initial_insert.sql
elif [ "$1" = "2" ]; then
    docker-compose run mssql-tools /opt/mssql-tools/bin/sqlcmd -S mssql -U SA -P Passw0rdOfs3cr3ts -i /data/2_update_data.sql
else
    echo "Invalid argument"
fi
