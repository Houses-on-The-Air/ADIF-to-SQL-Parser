import yaml

class ConfigLoader:
    """Loads database configuration from config.yaml."""

    @staticmethod
    def load_config():
        with open("config.yaml", "r") as file:
            return yaml.safe_load(file)
