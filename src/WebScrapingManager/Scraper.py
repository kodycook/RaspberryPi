# This is the Object which defines the scraper objects
class scraper:
    # The class "constructor" - It's actually an initializer
    def __init__(self, name, ID, URL, username, password, frequency):
        self.name = name
        self.ID = ID
        self.URL = URL
        self.username = username
        self.password = password
        self.frequency = frequency
