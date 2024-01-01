from XmlTree import XmlTree

referXml = XmlTree('refer.xml')
targetXml = XmlTree('target.xml')



for game in targetXml.game_tag_list:
    game_path = game.find('path')

    refer_game_name = referXml.get_name(game_path.text)
    if refer_game_name:
        print(refer_game_name)
        # game.set('name', refer_game_name)
        game.find('name').text = refer_game_name

    targetXml.tree.write('target.xml', encoding='utf8')

