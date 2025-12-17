s1="Make a lot of money"
s2="buy now"
s3="subscibe this"
s4="clik this"

message = input("Enter your message: ")
if((s1 in message), (s2 in message), (s3 in message), (s4 in message)):
    print("This is a spam")

else:
    print("This is not a spam")