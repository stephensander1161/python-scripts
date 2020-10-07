import boto3

client = boto3.client('s3')
path = 's3://NAMEOFBUCKET/KEYNAME.csv'
df = pd.read_csv(path)
df.head()
