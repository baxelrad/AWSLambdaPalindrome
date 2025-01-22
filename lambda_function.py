import json
import re
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

    try:
        s3_Bucket_Name = event["Records"][0]["s3"]["bucket"]["name"]
        s3_File_Name = event["Records"][0]["s3"]["object"]["key"]
        
        object = s3.get_object(Bucket=s3_Bucket_Name, Key=s3_File_Name)
        #print(s3_Bucket_Name)
        #print(s3_File_Name)
        body = object['Body']
        txt_string = body.read().decode('utf-8')
        #print(txt_string)
        txt_lines = txt_string.split('\n')
        #print(txt_lines)


        isPalindromeTest = []
        for x in txt_lines:
            isPalindromeTest.append(isPalindrome(x))
        print(isPalindromeTest)
        return {
            'statusCode': 200,
            'body': json.dumps(isPalindromeTest)
        }

    except Exception as err:
        print(err)

    return

def isPalindrome(s):

    cleanString = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    cleanLen = len(cleanString)

    for x in range(cleanLen//2):
        if (cleanString[x:x+1] != cleanString[cleanLen-x-1:cleanLen-x]):
            return False
    return True
