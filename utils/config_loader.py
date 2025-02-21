import yaml


class ConfigLoader:
    """
    ConfigLoader is a utility class for loading database configuration from a YAML file.

    Methods:
        load_config: Reads the 'config.yaml' file and returns its contents as a dictionary.
    """

    @staticmethod
    def load_config():
        """
        Load configuration from a YAML file.

        This function opens the "config.yaml" file in read mode and uses the
        PyYAML library to safely load and parse the YAML content.

        Returns:
            dict: The parsed configuration data from the YAML file.
        """
        with open("config.yaml", "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
