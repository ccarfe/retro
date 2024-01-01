import xml.etree.ElementTree as ET


class XmlController:
    def __init__(self, xml_file, game_tag='game'):
        self.xml_file = xml_file
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.game_tag_list = self.root.findall(game_tag)

    def get_name(self, search_game_path):
        for game in self.game_tag_list:
            path = game.find('path')
            path_text = path.text.replace('./', '')
            path_text = path_text.replace('../', '')
            if path_text == search_game_path:
                return game.find('name').text
        return None
