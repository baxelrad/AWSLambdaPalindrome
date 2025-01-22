Leetcode Palindrone problem adapted into an AWS Lambda function. Triggered by a .txt file being uploaded to an S3 bucket, it checks every line in the .txt to check if it is a palindrome.

sample input:
notapalindrome
maybeapalindrome
tacocat
racecar

sample output:
[False, False, True, True] 
