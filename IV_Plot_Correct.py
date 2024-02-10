#IV性能評価のプロット
#1行目...アノード電流
#2行目...アノード電位
#3行目...カソード電流
#4行目...カソード電位
#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#csvファイルのパス
csv_file_path = "C:\\Users\\eitat\\OneDrive\\ドキュメント\\ac.csv"

#csvファイルをデータフレームに読み込む
df = pd.read_csv(csv_file_path, header = None,index_col = None)

#電位を定義
Ea = df[1]
Ec = df[3]
print(Ea)
print(Ec)

#電流を定義
Ia = df[0]
Ic = df[2]
print(Ia)
print(Ic)

#アノードのIV特性のプロット
plt.plot(Ia, Ea, color='red',linewidth=5, label='anode')
plt.title('anode I-V')
plt.axvline(x=0, color='black', linestyle='-.', linewidth=1)
plt.axhline(y=0, color='black', linestyle='-.', linewidth=1)
plt.xlabel('Ia [mA]')
plt.ylabel('Ea [V]')
plt.legend()
plt.show()

#カソードのIV特性のプロット
plt.plot(Ic, Ec, color='blue',linewidth=5, label='cathode')
plt.title('cathode I-V')
plt.axvline(x=0, color='black', linestyle='-.', linewidth=1)
plt.axhline(y=0, color='black', linestyle='-.', linewidth=1)
plt.xlabel('Ic [mA]')
plt.ylabel('Ec [V]')
plt.legend()
plt.show()