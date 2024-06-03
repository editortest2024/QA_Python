def list_max (x: list):
    if (len(x)):
        x.sort(reverse=True)        
        return x[0]
    
z = [8, 10, 16, 1, 0]    
m = list_max(z)
print(f'{m} - наибольший элемент списка {z}')