import search
TIMEARRAY = [1451577600,1467302400,1483200000,1498838400,1514736000,1530374400,1546272000,1561910400,1577808000,1593532800,1609430400,1625068800,1640966400,1656604800,1672502400,1688140800,1704038400,1719763200,1735660800]
if __name__ == '__main__':
    '''主程序'''
    search.time_list_search(['川普','特朗普'], [(1451577600,1467302400),(1467302400,1483200000)], maxpage = 2)