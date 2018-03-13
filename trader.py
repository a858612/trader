
# You can write code above the if-main block.
import pandas as pd
if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
########################################################
df = pd.read_csv('testing_data.csv',header=None)
firstV= df.iloc[0,0]
out = df
leng = len(out)
##out.iloc[1,1] = 666
assets = 0
##print(out)
##leng = len(df)
holding = 0
NOACCTION = 1
lstBuy = firstV

##print(holding)
for i in range(0,leng):
    if i < leng-1 :

        if      (df.iloc[i,0]-lstBuy) > lstBuy*0.1:   ##sell
                if  holding > -1:
                    out.iloc[i,0] = -1
                    holding = holding - 1
                    lstBuy = df.iloc[i+1,0]
                    assets = assets + df.iloc[i+1,0]
                    NOACCTION = 0
        elif      (lstBuy - df.iloc[i,0]) > lstBuy*0.1:   ##buy
                if  holding < 1:
                    out.iloc[i,0] = 1
                    holding = holding + 1
                    lstBuy = df.iloc[i+1,0]
                    assets = assets - df.iloc[i+1,0]
                    NOACCTION = 0
        elif      df.iloc[i,0] < df.iloc[i,3] : ##up sell
            if  holding > -1:
                out.iloc[i,0] = -1
                holding = holding - 1
                assets = assets + df.iloc[i+1,0]
                NOACCTION = 0
        elif    df.iloc[i,0] > df.iloc[i,3] :##down   buy
            if  holding < 1:
                out.iloc[i,0] = 1
                holding = holding + 1
                assets = assets - df.iloc[i+1,0]
                NOACCTION = 0
        if NOACCTION == 1:
                out.iloc[i,0] = 0
        NOACCTION = 1

if holding == -1:
    assets = assets - df.iloc[leng-1,0]
    holding = 0
elif holding == 1:
    assets = assets + df.iloc[leng-1,0]
    holding = 0
out = out.ix[:leng-2, 0]
out = out.astype(int)
###############################67    109
print(out)
print("assets  ", assets)
print("holding ",holding)
out.to_csv("output.csv")
