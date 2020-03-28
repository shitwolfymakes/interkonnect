import os.path
import json


def main():
    if os.path.exists("ik_properties.json"):
        with open("ik_properties.json") as ik_props:
            data = json.load(ik_props)
#end main


if __name__ == "__main__":
    main()
