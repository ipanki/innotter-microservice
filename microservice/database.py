import boto3
from microservice import config


def connect_db():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY, region_name=config.AWS_SES_REGION)
    return dynamodb


def get_or_create_table_post(dynamodb):
    for table in dynamodb.tables.all():
        if table.name == 'Statistics':
            print('Table Post already exists')
            return table

    table = dynamodb.create_table(
        TableName='Statistics',
        KeySchema=[
            {
                'AttributeName': 'page_id',
                'KeyType': 'HASH'
            },
            {
                "AttributeName": "user_id",
                "KeyType": "RANGE"
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'page_id',
                'AttributeType': 'S'
            },
            {
                "AttributeName": "user_id",
                "AttributeType": "N"
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print('Table Post has been created')
    return table
