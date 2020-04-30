# User
if you don't know how to get your token or xsessionid, go to the [**faq**](api/other/faq)

`userSignup(email)` - Sign up for an account. Email will be sent a confirmation code.

`userConfirmEmail(code, password)` - Confirm your email and create a password.

`userLogin(email, password)` - Login with your email and password, returns your info.

`ghostLogin(self, xsessionid)` - Login with your session id.

`getUserByID(token, xsessionid, userid)` - Get information about a user.