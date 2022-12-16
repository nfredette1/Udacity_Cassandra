#!/usr/bin/env python
import snowflake.connector
import pandas as pd

# Gets the version
ctx = snowflake.connector.connect(
    user='KA_ODS_RW_PROD_USER',
    password='@Dj92b1ywTuWyh22',
    account='libertymutual-corp_aps_us_east_1'
    )
cs = ctx.cursor()

sql =  """
        WITH SUPPORTGRP AS
            (SELECT SUPPORTGROUPID AS "Support Group ID"
            ,SUPPORTGROUPROLE AS "Support Role"
            ,ORGANIZATION AS "Organization"
            ,"STATUS" AS "Status"
            ,SUPPORTGROUPSLO "Support Group SLO"
            ,SUPPORTGROUPMANAGER "Support Group Manager"
            ,SUPPORTGROUPEMAIL "Support Group Email"
            ,LASTMODIFIEDDATE "Last Modified Date"
            ,DESCRIPTION "Description"
            ,SUPPORTGROUPNAME   "Group Name"
            ,ROW_NUMBER() OVER (PARTITION BY SUPPORTGROUPID ORDER BY LASTMODIFIEDDATE DESC) AS "ROW_NUMBER"
        FROM "IT_ODS_PROD"."CORP_IT_ODS"."REMEDY_CTM_SUPPORTGROUP")
        SELECT *
        FROM SUPPORTGRP
        WHERE ROW_NUMBER = 1
    """

try:
    cs.execute(sql)
    one_row = cs.fetchall()
    print(one_row[0])
finally:
    cs.close()
ctx.close()

df = pd.DataFrame(one_row)