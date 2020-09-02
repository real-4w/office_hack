import whois
domain = whois.query('nzx.com')

print(domain.__dict__)
print(domain.name, domain.name_servers)
