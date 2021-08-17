#pandenado
import pandas as pd


hoja_csv='libros'

csv=pd.read_csv(hoja_csv+'.txt',sep=';')

isbnd=9788471537591

fila_isbn=csv[csv.isbn==isbnd]

num_tit=1
num_aut=2
num_edit=3
num_pre=5
num_tem =9

tit = fila_isbn.iat[0,int(num_tit)]
aut = fila_isbn.iat[0,int(num_aut)]
edit = fila_isbn.iat[0,int(num_edit)]
pre = fila_isbn.iat[0,int(num_pre)]
tem = fila_isbn.iat[0,int(num_tem)]	

print(tit)