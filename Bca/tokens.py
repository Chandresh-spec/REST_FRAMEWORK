
from rest_framework_simplejwt.tokens import RefreshToken


class  CustomToken(RefreshToken):

    @property

    def payload(self):
        data=super().payload

        data['role']=self.user.role

        return data
