#!/usr/bin/env python
import snowflake.connector
import pandas as pd
import numpy as np
#import pyarrow
#from snowflake.connector.pandas_tools

snowflakePort = 443
snowflakeAccount = 'libertymutual-corp_aps_us_east_1'
snowflakeWarehouse = 'IT_ODS_QRY_WH'
snowflakeDatabase = 'IT_ODS_PROD'
snowflakeSchema = 'CORP_IT_ODS'
snowflakeRole = 'IT_ODS_PROD_RL'

conn = snowflake.connector.connect(
    authenticator='externalbrowser',
    user = input('Email address: '),
    account = snowflakeAccount,
    database = snowflakeDatabase,
    warehouse = snowflakeWarehouse,
    schema = snowflakeSchema,
    role = snowflakeRole,
    numpy=True
)