
from client import Client 
from social_network import Social_network

class ClientSocialNetwork:
    def __init__(self, client: Client, social_network: SocialNetwork):
        self.client = client
        self.social_network = social_network

    def get_client(self):
        return self.client

    def set_client(self, client: Client):
        self.client = client

    def get_social_network(self):
        return self.social_network

    def set_social_network(self, social_network: SocialNetwork):
        self.social_network = social_network
