import sys
import logging
import pymysql
import json
import os

#rds settings
rds_endpoint = os.environ['rds_endpoint']
username=os.environ['username']
password=os.environ['password']
db_name=os.environ['db_name']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Connection
try:
    connection = pymysql.connect(host=rds_endpoint, user=username,
        passwd=password, db=db_name)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def handler(event, context):
    cur = connection.cursor()  
## Retrieve Data
    query = "SELECT * FROM Branch where clinicId='{}'".format(event['clinicId'])    
    cur.execute(query)
    connection.commit()
## Construct body of the response object
    
    branchList = []
    rows = cur.fetchall()
    for row in rows:
        print("TEST {0} {1} {2} {3} {4} {5} {6} {7} {8}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
        transactionResponse = {}
        transactionResponse = {}
        transactionResponse['id'] = row[0]
        transactionResponse['name'] = row[1]
        transactionResponse['district'] = row[2]
        transactionResponse['addr'] = row[3]
        transactionResponse['postal'] = row[4]
        transactionResponse['contactNo'] = row[5]
        transactionResponse['latt'] = row[6]
        transactionResponse['longt'] = row[7]
        transactionResponse['clinicId'] = row[8]
        branchList.append(transactionResponse)

# Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type']='application/json'
    responseObject['headers']['Access-Control-Allow-Origin']='*'
    responseObject['body']= branchList
    # responseObject['body'] = json.dumps(transactionResponse, sort_keys=True,default=str)
    
    #k = json.loads(responseObject['body'])
    #print(k['uin'])

    return responseObject