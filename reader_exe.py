
def readZeroEnded(data, pos, endpos):
    out = []
    while pos < endpos:
        s = ''
        while pos < endpos and data[pos] != 0:
            s += chr(data[pos])
            pos += 1
        if pos < endpos:
            pos += 1
        out.append(s)
    return out

def readData(dlPath):
    fname = dlPath + '/darkland.exe'
    data = map(ord, open(fname).read())
    out = {}

    #bg card fnames
    pos = 0x0018b710
    end = 0x0018c157
    out['bg_cards'] = readZeroEnded(data, pos, end)

    '''
month names
0x00187d00
0x00187d56

protection symbols names
0x00187d56
0x00187e12

alchemy menu opts?
0x00187e12
0x00187e5f

load game menu opts
0x00187e5f
0x00187e9e

character add menu opts
0x00187e9e
0x00187f26

... other menu opts

some action/quest related strings
0x0018804f
0x001881d9

character attribute names
0x001881d9
0x00188222

skills
0x00188222
0x001882f0

Menu opts,
occupation names
daemon names

0x001882f0
...


card variable names
0x00188af4
0x00188dd2 ??

city/village ruller titles?

male first names
0x00188e71
0x001891a0

female first names
0x001891a0
0x0018945f

surnames
0x0018945f
0x00189a20

some game menus & msgs
0x00190fca

battle data (debug print?)
0x0019298a

files for map
0x00193685
0x001937ae


0x001937c6

pictures for inventory + texts (atts, skill abbrs)
0x00193844
0x00193cd8

buy/sell
0x00193cd8
0x00193fc2

alchemy
0x00193fc2
0x001941ae

saint texts, pics...
0x001941ae

party info texts
0x001943ec

cache operations
0x001945b8

gasthaus stay opts and texts
0x001947ec

camp opts and texts
0x00194ac2
    '''
    # msg card names + comments or what?
    pos = 0x00196502
    end = 0x0019783f
    #out['msg_cards'] = [t.upper() if t.startswith('$') else t for t in readZeroEnded(data, pos, end)]
    out['msg_cards'] = [t.upper() for t in readZeroEnded(data, pos, end) if t.startswith('$')]

    return out

def ps(s):
    out = ''
    for ch in s:
        o = ord(ch)
        if ch >= ' ' and o < 127:
            out += ch
        else:
            out += '<'+str(o)+'>'
    return out


# main ------------
if __name__ == '__main__':
    import sys
    from utils import itemStr

    dlPath = sys.argv[1] if len(sys.argv) > 1 else 'DL'

    data = readData(dlPath)

    # print data
    #for i, s in enumerate(data['bg_cards']):
    #    print '%4d %s'%(i, ps(s))

    print

    for i, s in enumerate(data['msg_cards']):
        print '%4d %s'%(i, ps(s))


