from datetime import datetime


def thamdu(name):
    with open('thamdu.csv', 'r+') as f:
        myDataList = f.readlines()
        print(myDataList)
        nameList = []
        for line in myDataList:
            entry = line.split(',') # tách theo dấu ,
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S') # biểu thị string giờ phút giây
            f.writelines(f'\n{name},{dtString}')