import numpy as np
import pprint
import os 

def tack1():
    np.random.seed(1000)
    outfile='file_dan1'
    m = np.random.randn(15,15)
#    print(m)
    np.save(outfile, m)
    m0=np.load(outfile+".npy")
#    print("*"*50,"\n", m0)
    z = m - m0
#    print("*"*50,"\n", z)
 #Считайте массив из файла, с использованием целочисленного типа данных ???? 
# Если речь, о записи данных, в формате double float а считываем в формате int
# то будет ошибка если считать и преобразовать в цело численные? тогда формулировка не правильная
# проверьте условие 
    z1=np.abs(m- np.array(m0, int)).sum()
    print("*"*50,"\n", z1)
#Формат ответа: Число (например, 102.4)    


def _tack2(n ):
    np.random.seed(1000)
    m = np.random.randn(n)
    np.save('file_dan_01', m) 
    np.savez_compressed('file_dan_02', m)
    size1=os.path.getsize('file_dan_01.npy') 
    size2=os.path.getsize('file_dan_02.npz') 
    print(" Вариант при n = {}  file_dan_01-file_dan_02 = {} разница в байтах ".format(n, size1-size2))
    return

def tack2():
    _tack2(100 )
    _tack2(1000000 )
# Вариант при n = 100  file_dan_01-file_dan_02 = -114 разница в байтах
# Вариант при n = 1000000  file_dan_01-file_dan_02 = 314227 разница в байтах


if __name__ == "__main__":
#    tack1()
    tack2()
