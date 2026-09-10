has_account = True
email_verified = False
can_login = has_account and email_verified
print("can_login", can_login)
email = "g@example.com"
is_email_valid ="@" in email
print("is_email_valid", is_email_valid)
user_age = 17
is_age_valid = user_age >= 18
print("is_age_valid", is_age_valid)
print("can_login and is_email_valid", can_login and is_email_valid)

print("has_account is true", has_account is True)