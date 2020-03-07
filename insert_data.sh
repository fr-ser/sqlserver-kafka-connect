#!/bin/bash

if [ "$1" = "1" ]; then
    docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/1_initial_insert.sql
elif [ "$1" = "2" ]; then
    docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/2_update_data.sql
elif [ "$1" = "3" ]; then
    docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/3_delete_data.sql
else
    echo "Invalid argument"
fi
