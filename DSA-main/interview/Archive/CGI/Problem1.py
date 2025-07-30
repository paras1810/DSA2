import view 
from Usermodels import Users

@view
def get_user_details():
    Users.objects.filter(pk=1)
