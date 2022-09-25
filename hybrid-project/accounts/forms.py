from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    password=None
    # password = ReadOnlyPasswordHashField(
    #     label=("Password"),
    #     help_text=(
    #         #'Raw passwords are not stored, so there is no way to see this '
    #         #'user’s password, but you can change the password using '
    #         #'<a href={}>비밀번호 변경</a>.'
    #         '<a href={}></a>'
    #     ),
    # )
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
        #exclude = ('email','password',)
        