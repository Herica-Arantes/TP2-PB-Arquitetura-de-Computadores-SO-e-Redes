git remote add origin https://github.com/Herica-Arantes/TP2-PB-Arquitetura-de-Computadores-SO-e-Redes.git
git branch -M main
git push -u origin mainimport psutil

interfaces = psutil.net_if_addrs()

for inter in interfaces:
    print(inter)
print("\nInformações sobre a interface Wi-Fi")
print("Endereço físico:", interfaces["Wi-Fi"][0].address)
print("Endereço IP:", interfaces["Wi-Fi"][1].address)
print("Endereço IPv6:", interfaces["Wi-Fi"][2].address)