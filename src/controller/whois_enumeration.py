import whois

class WhoisConfig:
    def __init__(self,target):
        self.target_domain =target

    def whois_search(self):
        response = whois.whois(self.target_domain)
        print(response)
if __name__ == "__main__":

    domain_name=WhoisConfig(".com")
    domain_name.whois_search()