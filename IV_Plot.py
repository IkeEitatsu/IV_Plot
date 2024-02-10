#IV性能評価のプロット
#1行目...アノード電位
#2行目...アノード電流
#3行目...カソード電位
#4行目...カソード電流
#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#csvファイルのパス
csv_file_path = "C:\\Users\\eitat\\OneDrive\\ドキュメント\\ac.csv"

#csvファイルをデータフレームに読み込む
df = pd.read_csv(csv_file_path, header = None,index_col = None)

#アノード電流にマイナスを乗算
Ea = -1*df[0]
Ec = df[2]
print(Ea)
print(Ec)

#電流単位をmAに変換、カソード電流にマイナスを乗算
Ia = df[1]
Ic = -1*df[3]
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