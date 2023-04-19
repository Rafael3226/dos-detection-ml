import pandas as pd

remove = [
    'average packet size',
    'avg fwd segment size'
]

files = ['training.csv', 'test.csv']


for file in files:
    fileDir = './processed/' + file
    # load the dataframe from a CSV file
    df = pd.read_csv(fileDir)

    # remove the variables not available in this implementation
    df = df.drop(columns=remove)

    # save the updated dataframe to a new CSV file
    df.to_csv(fileDir, index=False)


# all = ['destination port',
#        'total length of fwd packets',
#        'fwd packet length max',
#        'fwd packet length mean',
#        'fwd packet length std',
#        'bwd packet length max',
#        'bwd packet length min',
#        'bwd packet length mean',
#        'bwd packet length std',
#        'bwd iat total',
#        'bwd iat mean',
#        'bwd iat std',
#        'bwd iat max',
#        'fwd psh flags',
#        'min packet length',
#        'max packet length',
#        'packet length mean',
#        'packet length std',
#        'packet length variance',
#        'syn flag count',
#        'psh flag count',
#        'urg flag count',
#        'down/up ratio',
#        'average packet size',
#        'avg fwd segment size',
#        'avg bwd segment size',
#        'subflow fwd bytes',
#        'min_seg_size_forward']


# cal = ['destination port',
#        'subflow fwd bytes',]
