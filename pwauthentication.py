import getpass

database = {"test.user":"123456", "est.user":"1234567", "st.user":"12345"}
username = input ("Enter your Username:")
password = getpass.getpass ("Enter your password:")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass ("Enter your password again:")
        break 

print("Verified")
