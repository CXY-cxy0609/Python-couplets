def conclude(s):                                                                                      #对词性适当归类
    if s == 'ad' or s == 'ag' or s == 'an':
        s = 'a'
    elif s == 'q':
        s = 'mq'
    elif s == 'df' or s == 'dg':
        s = 'd'
    elif s == 'h' or s == 'j' or s == 'k' or s == 'y' or s == 'yg':
        s = 'n'
    elif s == 'mg':
        s = 'm'
    elif s == 'rg' or s == 'rz' or s == 'rr':
        s = 'r'
    elif s == 'vd' or s == 'vi' or s == 'vq' or s == 'p' or s == 'ud' or s == 'ug' or s == 'ul' \
            or s == 'uj' or s == 'uv' or s == 'uz' or s == 'u' or s == 'l' or s == 'f':
        s = 'v'

    return s
nature = ['a','ad','ag','an','b','c','d','df','dg','e','f','g','h','i','j','k','l','m','mg',
          'mq','n','ng','nr','nrfg','nrt','ns','nt','nz','o','p','q','r','rg','rr','rz','s',
          't','tg','u','ud','ug','uj','ul','uv','uz','v','vd','vg','vi','vn','vq','x','y','z','zg']   # 词的所有属性