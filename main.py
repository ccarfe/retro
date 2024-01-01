import os

from xml_controller import XmlController


if __name__ == '__main__':
    while True:
        refer_xml_file_path = input('Please input reference XML file path: ')
        target_xml_file_path = input('Please input target XML file path: ')
        # referXml = XmlController('refer.xml')
        # targetXml = XmlController('target.xml')

        referXml = XmlController(refer_xml_file_path)
        targetXml = XmlController(target_xml_file_path)

        game_count = 0
        name_change_count = 0

        no_changed_game_list = []
        changed_game_list = []

        target_xml_file_dir = os.path.dirname(target_xml_file_path)
        result_txt_output = target_xml_file_dir + '\\resul.txt'
        f = open(result_txt_output, 'w', encoding='utf8')

        for game in targetXml.game_tag_list:
            game_path = game.find('path')
            print(game_path.text)
            game_path_txt = game_path.text.replace('./', '')
            game_path_txt = game_path_txt.replace('../', '')

            refer_game_name = referXml.get_name(game_path_txt)
            if refer_game_name:
                temp_game_txt = game.find('name').text
                game.find('name').text = refer_game_name
                print(f'{temp_game_txt} => {refer_game_name}')
                changed_game_list.append(f'{temp_game_txt} => {refer_game_name}')
                name_change_count += 1
            else:
                no_changed_game_list.append(game_path.text)

            game_count += 1

        targetXml.tree.write(target_xml_file_path, encoding='utf8')

        print('\n\n')
        print('=' * 50)
        print(f'대상 게임 수: {game_count}\n이름 변경 횟수: {name_change_count}')
        f.write(f'\n대상 게임 수: {game_count}\n이름 변경 횟수: {name_change_count}\n')
        print(f'변경 되지 않은 게임리스트')
        f.write(f'변경 되지 않은 게임리스트: {game_count - name_change_count}\n')
        for elem in no_changed_game_list:
            print(elem)
            f.write(elem + '\n')

        f.write(f'\n\n변경 리스트\n')
        for elem in changed_game_list:
            f.write(elem + '\n')

        f.close()
        print('\n\n\n')