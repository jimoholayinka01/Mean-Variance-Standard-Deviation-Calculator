import numpy as np

def calculate(list):
    if len(list)==9:
        new_array = np.array(list).reshape(3,3)
        new_array=new_array
        calculations = {'mean':[new_array.mean(axis=0).tolist(),new_array.mean(axis=1).tolist(),new_array.mean().tolist()],'Variance':[new_array.var(axis=0).tolist(),
        new_array.var(axis=1).tolist(),new_array.var().tolist()],'Standard Variation':[new_array.std(axis=0).tolist(),
        new_array.std(axis=1).tolist(),new_array.std().tolist()],'Max':[new_array.max(axis=0).tolist(),
        new_array.max(axis=1).tolist(),new_array.max().tolist()],'Min':[new_array.min(axis=0).tolist(),
        new_array.min(axis=1).tolist(),new_array.min().tolist()],'Sum':[new_array.sum(axis=0).tolist(),
        new_array.sum(axis=1).tolist(),new_array.sum().tolist()]}
        return calculations
    else:
        print('List must contain nine numbers.')

# def calculate(list):
#     # print(list)
#     new_array = np.array(list)
#     new_array = np.array(list).reshape(3,3)
#     print(new_array.ndim)
#     calculations = {'mean':[new_array.mean(axis=0).tolist(),new_array.mean(axis=1).tolist(),new_array.mean()],'Variance':[new_array.var(axis=0).tolist(),
#     new_array.var(axis=1).tolist(),new_array.var()],'Standard Variation':[new_array.std(axis=0).tolist(),
#     new_array.std(axis=1).tolist(),new_array.std()],'Max':[new_array.max(axis=0).tolist(),
#     new_array.max(axis=1).tolist(),new_array.max()],'Min':[new_array.min(axis=0).tolist(),
#     new_array.min(axis=1).tolist(),new_array.min()],'Sum':[new_array.sum(axis=0).tolist(),
#     new_array.sum(axis=1).tolist(),new_array.sum()]}



#     return calculations