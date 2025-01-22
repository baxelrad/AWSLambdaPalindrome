Leetcode Palindrone problem adapted into an AWS Lambda function. Triggered by a .txt file being uploaded to an S3 bucket, it checks every line in the .txt to check if it is a palindrome.<br><br>

sample input:<br><br>
notapalindrome<br>
maybeapalindrome<br>
tacocat<br>
racecar<br>
<br><br>
sample output:<br>
[False, False, True, True] 
