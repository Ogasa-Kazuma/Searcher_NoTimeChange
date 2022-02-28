
import importlib
import Pickle_Reader
import os, sys
sys.path.append(os.pardir + "/PollutionCreater3D")

import Pollution
importlib.reload(Pollution)
from Pollution import Pollution


importlib.reload(Pickle_Reader)

import Pollution_Data_Loader
importlib.reload(Pollution_Data_Loader)



pklReader = Pickle_Reader.PickleReader()
pollutionDataLoader = Pollution_Data_Loader.PollutionDataLoader(pklReader)
#ファイルからデータを読み出す.読み出したデータは「Pollutionオブジェクト」として返される
#よって、下記 pollutionsはSaveやViewメソッドを使用することができる
pollutions = pollutionDataLoader.Load("../PollutionCreater3D/PollutionLog/unko.pkl")

#読み込んだ濃度値ファイルから、値を読み出す
print("x:0, y:0, z:0の濃度値" + str(pollutions.GetPollution(x = 0, y = 0, z = 1)))
print("x:10, y:10, z:10の濃度値" + str(pollutions.GetPollution(x = 10, y = 10, z = 10)))
