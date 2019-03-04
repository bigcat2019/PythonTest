# coding:utf-8
import sys
from Library.BaiduIndex import *

def Main(argv=None):
    print("开始查询相关信息；").decode('UTF-8').encode('GBK') 
    # 百度风云榜所有榜单
    url = "http://top.baidu.com/boards?fr=topindex"
    result = SelectBoards()
    print("Board Have "+str(result[0])+" Data;")
    if result[0]==0:
        GatherBoard()
    else:
        BoardInfos=SelectBoardInfos()
        for item in BoardInfos:
            GatherBoardTop(item)
    print("Run SUCCESS!")       
    
if __name__ == "__main__":
    sys.exit(Main())

