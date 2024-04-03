import xml.etree.ElementTree as ET

class Configuration:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config = self._parse_config()

    def _parse_config(self):
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()
            config = {}
            for service in root:
                service_name = service.tag
                service_config = {}
                for child in service:
                    service_config[child.tag] = child.text.strip()
                config[service_name] = service_config
            return config
        except Exception as e:
            print(f"Error parsing configuration file: {e}")
            return {}

    def get_config(self, service_name):
        return self.config.get(service_name, {})
    
