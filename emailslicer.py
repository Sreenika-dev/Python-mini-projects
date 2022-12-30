user_email =  input("Email address: ").strip() #strip = removes whitespaces before and after a string
print(user_email)
username =  user_email[0:user_email.index("@")]
domainname =  user_email[user_email.index("@")+1:]
message =  f"{username} is username and {domainname} is domain name of the received address"
print(message)