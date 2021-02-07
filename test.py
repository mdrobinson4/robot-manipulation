import pickle
import sympy
  
def storeData(dh):
    dbfile = open('examplePickle', 'ab') 
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
    for keys in db: 
        print(keys, '=>', db[keys]) 
    dbfile.close() 
  
if __name__ == '__main__': 
    th1, th2, th3, th4, th5, th6 = sympy.symbols("th1, th2, th3, th4, th5, th6")
    abb_dh = {
        'a': [0, -90, 0, -90, 90, -90],
        'alpha': [0, 320, 975, 280, 0, 0],
        'd': [0, 0, 0, 887, 0, 0],
        'theta': [th1, th2, th3, th4, th5, th6]
    }
    storeData(abb_dh) 
    loadData() 