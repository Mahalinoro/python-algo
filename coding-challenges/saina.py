# Manamboara sainam-pirenena Malagasy amin'ny alalan'ny ASCII Art raha homena ny alehibeny n.

# N.B: n dia sakan'ny ("largeur") "bande" iray miaraka amin'ny sisiny, izany hoe sakan'ny bande fotsy/maitso/mena miaraka amin'ny sisiny 
# (Jereo ny exemple mba ahazoana azy tsara)

# Ny characters ampiasaina:
# # : ny sisiny sy ny fisarahan'ny loko
# - : loko maitso
# . : loko fotsy
# * : loko mena

# Example

# For n = 5, the answer should be
# ["############",
#  "#...#******#",
#  "#...#******#",
#  "#...#******#",
#  "#...########",
#  "#...#------#",
#  "#...#------#",
#  "#...#------#",
#  "############"]

def sainamPirenena(n):
    sisiny = '#'
    maitso = '-'
    fotsy = '.'
    mena = '*'
    
    n_fotsy = n - 2
    n_mena = 2 + (2*(n-3))
    h = 3 + (n_fotsy * 2)
    w = 3 + n_fotsy + n_mena
    
    saina = []
    
    for i in range(h):
        if i == 0 or i == h-1:
            saina.append(sisiny * w)
        elif i > 0 and i < math.floor(h//2):
            saina.append(sisiny + (fotsy * n_fotsy)+ sisiny +(mena * n_mena) + sisiny)
        elif i > math.ceil(h // 2) and i < h:
            saina.append(sisiny + (fotsy * n_fotsy) + sisiny + (maitso * n_mena) + sisiny)
        else:               
            saina.append(sisiny + (fotsy * n_fotsy) + (sisiny * (w - n_fotsy - 1)))
    
    return saina
        