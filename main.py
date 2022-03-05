
#################### 標準ライブラリ #######################
#システム関連
import importlib
import os, sys
sys.path.append(os.pardir + "/PollutionCreater3D")
#数値計算
import random
#######################################################

#################### 自作モジュール ########################
import Pollution
importlib.reload(Pollution)
from Pollution import Pollution

import Pickle_Reader
importlib.reload(Pickle_Reader)

import Pollution_Data_Loader
importlib.reload(Pollution_Data_Loader)
###########################################################



#################### main ################################

def main():

    #pkl形式で保存している濃度データを読み取る
    #Pickle_Readerはpklファイルを「開く」ことしかできないので、
    #その開いたファイルから濃度値をプログラムで読み取れる形式に変換するのがPollution_Data_Loader
    pklReader = Pickle_Reader.PickleReader()
    pollutionDataLoader = Pollution_Data_Loader.PollutionDataLoader(pklReader)
    
    #読み出したデータは「Pollutionオブジェクト」として返される
    #よって、下記 pollutionsはSaveやViewメソッドを使用することができる
    pollutions = pollutionDataLoader.Load("../PollutionCreater3D/PollutionLog/pData.pkl")

    #読み込んだ濃度値ファイルから、値を読み出す
    #このように一点一点の濃度を調べることにより汚染源を探します
    print("x:0, y:0, z:0の濃度値" + str(pollutions.GetPollution(x = 0, y = 0, z = 1)))
    print("x:10, y:10, z:10の濃度値" + str(pollutions.GetPollution(x = 10, y = 10, z = 10)))

########################################################
if __name__ == "__main__":
    main()
