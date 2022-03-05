
#################### 標準ライブラリ #######################
#システム関連
import importlib
import os, sys
sys.path.append(os.pardir + "/PollutionCreater3D")
#数値計算
import random
import matplotlib.pyplot as plt
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


def CreaterGraphObject():
    fig = plt.figure()
    graph_object = fig.add_subplot(111, projection = '3d')
    graph_object.set_xlabel('x [m]')
    graph_object.set_ylabel('y [m]')
    graph_object.set_zlabel('z [m]')
    return graph_object



#################### main ################################

def main():

    #このプログラムでは、汚染源探索のプログラムをどう組めばいいか、かなり簡潔に説明します
    #1.まず濃度値をファイルから読み出す必要があります。そのためにPollution_Data_Loaderクラスを用意しました
    #このクラスは、時間変化を考慮していない濃度分布モデルのファイルにのみ対応しています
    #2.濃度ファイルからちゃんと値を読み込めているか、Viewメソッドで確認します
    #このプログラムでは、ただ濃度ファイルから読み取るだけでなく、読み取った濃度や座標を、内部でPollutionオブジェクトに
    #変換してくれるため、Save, Viewメソッドなどがそのまま使えます
    #3.GetPollutionメソッドを使って、指定した座標の濃度値を取得します
    #具体的に、どのような座標を順に進んでいくか、についてはおまかせします


    #pkl形式で保存している濃度データを読み取る
    #Pickle_Readerはpklファイルを「開く」ことしかできないので、
    #その開いたファイルから濃度値をプログラムで読み取れる形式に変換するのがPollution_Data_Loader
    pklReader = Pickle_Reader.PickleReader()
    pollutionDataLoader = Pollution_Data_Loader.PollutionDataLoader(pklReader)

    #読み出したデータは「Pollutionオブジェクト」として返される
    #よって、下記 pollutionsはSaveやViewメソッドを使用することができる
    pollutions = pollutionDataLoader.Load("../PollutionCreater3D/PollutionLog/pData.pkl")
    graph_object = CreaterGraphObject()
    pollutions.View(graph_object, pollution_lower_limit = 10)

    #読み込んだ濃度値ファイルから、値を読み出す
    #このように一点一点の濃度を調べることにより汚染源を探します
    print("x:0, y:0, z:0の濃度値" + str(pollutions.GetPollution(x = 0, y = 0, z = 1)))
    print("x:10, y:10, z:10の濃度値" + str(pollutions.GetPollution(x = 10, y = 10, z = 10)))

########################################################
if __name__ == "__main__":
    main()
