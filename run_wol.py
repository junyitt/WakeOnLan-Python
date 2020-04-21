from wol import wake_on_lan
import json

if __name__ == "__main__":
    with open("mac_list.json") as file:
        x = json.load(file)
        mac_list = list(x.values())

    for mac in mac_list:
        wake_on_lan(mac)