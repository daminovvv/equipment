from rest_framework.authentication import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    """Custom Authentication with Bearer token"""

    keyword = "Bearer"
