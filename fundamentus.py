# https://pypi.org/project/fundamentus/

import fundamentus

dfraw = fundamentus.get_resultado_raw()
print(dfraw.columns)

df = fundamentus.get_resultado()
print(df.columns)

# com filtro
print( df[ df.pl > 0] )

# por papel
dfp = fundamentus.get_papel('BBAS3')
dfp

dfps = fundamentus.get_papel(['BBAS3','PETR4'])
dfps

# por setores
setor1 = fundamentus.list_papel_setor(1) 
setor1 
setor2 = fundamentus.list_papel_setor(2)  
setor2

dfsetor = fundamentus.get_papel(setor1)
dfsetor
