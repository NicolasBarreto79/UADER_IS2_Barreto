import os
import platform

class Ping:
    def execute(self, ip_address: str):
        if not ip_address.startswith("192."):
            print(f"Dirección no permitida: {ip_address}")
            return
        print(f"Haciendo ping a {ip_address} (con control de dirección)...")
        self._do_ping(ip_address)

    def executefree(self, ip_address: str):
        print(f"Haciendo ping a {ip_address} (sin control de dirección)...")
        self._do_ping(ip_address)

    def _do_ping(self, ip_address: str):
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = f"ping {param} 10 {ip_address}"
        os.system(command)

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address: str):
        if ip_address == "192.168.0.254":
            print("IP especial detectada. Redirigiendo ping a www.google.com usando executefree...")
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)


proxy = PingProxy()

# Caso permitido
proxy.execute("192.168.0.1")  # Realiza ping normalmente

# Caso IP especial
proxy.execute("192.168.0.254")  # Redirige a www.google.com

# Caso bloqueado (por no iniciar con "192.")
proxy.execute("10.0.0.1")  # Rechazado
