import xml.etree.ElementTree as ET


class XmlTree:
    def __init__(self, xml_file, game_tag='game'):
        self.xml_file = xml_file
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.game_tag_list = self.root.findall(game_tag)

    def get_name(self, search_game_path):
        for game in self.game_tag_list:
            path = game.find('path')
            if path.text == search_game_path:
                return game.find('name').text
        return None