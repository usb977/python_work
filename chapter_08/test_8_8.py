def make_album(singer_name,album_name,num = None):
    album = {
        'singer':singer_name,
        'album':album_name,
    }
    if(num != None):
        album['song_num']=num
    return album

while True:
    print('\n下面请根据提示输入一张专辑信息，任何时候输入q即可退出程序！')

    singer = input('\n请输入歌手的名字：')
    if singer == 'q':
        break
    album = input('\n请输入专辑的名字：')
    if album == 'q':
        break

    album_dic = make_album(singer,album)

    print('\n您输入的专辑信息为：')
    for key,value in album_dic.items():
        print(f'\t{key.title()}: {value}')