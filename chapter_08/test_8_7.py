def make_album(singer_name,album_name,num = None):
    album = {
        'singer':singer_name,
        'album':album_name,
    }
    if(num != None):
        album['song_num']=num
    return album

album_dic = make_album('Jay Zhou','Still Fantasy',5)

print('\n专辑信息为：')
for key,value in album_dic.items():
    print(f'\t{key.title()}: {value}')