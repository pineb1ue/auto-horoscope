import yaml

with open("app/config/messages.yaml", "r") as yml:
    logging_conf = yaml.safe_load(yml)
