import dns.resolver

class DnsConfig:
    def __init__(self, target):
        self.target = target
        self.record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

    def dns_search(self):
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = ['8.8.8.8']  # Usar Google DNS
        resolver.timeout = 10  # Aumentar el tiempo de espera a 10 segundos

        for record_type in self.record_types:
            print(f"Consultando registros {record_type}...")
            try:
                answers = resolver.resolve(self.target, record_type)
            except (dns.resolver.NoAnswer, dns.exception.Timeout):
                print(f"No hay respuesta o tiempo de espera agotado para registros {record_type}")
                continue

            print(f"Registros {record_type} para {self.target}")
            for data in answers:
                print(f"{data}")
            print()  # Agregar una línea en blanco entre tipos de registros

if __name__ == "__main__":
    D = DnsConfig(".com")
    D.dns_search()