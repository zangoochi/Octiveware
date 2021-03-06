#=====================================================================================================
#Description:
#Django form for creating new users and for changing passwords 
#=====================================================================================================

#Edited by: Zach Montgomery
#Date:10/20/14
#Contact Info: zmontgom@kent.edu
#Changes made: Added ChangeEmailForm to provide the form for a user to change his/her email address.


#Edited by: Zach Montgomery	
#Date:10/28/14
#Contact Info: zmontgom@kent.edu
#Changes made: Added dynamic choices instead of hard coded ones
#=====================================================================================================


from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError

class NewUserForm(forms.Form):
    error_css_class = 'error'
    
    username = forms.CharField(label="username", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField()


class ChangeEmailForm(forms.Form):
	error_css_class = 'error'

	new_email = forms.EmailField()
	email_confirmation = forms.EmailField()

	def clean_email_confirmation(self):
		newEmail_cleaned = self.cleaned_data.get('new_email')
		confirmedEmail = self.cleaned_data.get('email_confirmation')

		if newEmail_cleaned != confirmedEmail:
			raise ValidationError("Email addresses do not match!")
		else:
			return newEmail_cleaned
