
import importlib
import os, sys
#pythonはデフォルトでは、上の階層にあるフォルダのファイルを読み取れないので、検索パスを追加する必要があります
sys.path.append(os.pardir + "/PollutionCreater3D")

import Pollution
importlib.reload(Pollution)
from Pollution import Pollution


class PollutionDataLoader:

    def __init__(self, pollutionFileReader):
        self.__pollutionFileReader = pollutionFileReader

    def Load(self, filePath):
        pollutionFile = self.__pollutionFileReader.Read(filePath)
        #最後の'pollution'のところは絶対に変更しないでください
        pollutionLog = self.__ReadPollutionLogFromFile(pollutionFile, 'pollution')
        return Pollution(pollutionLog)


    def __ReadPollutionLogFromFile(self, pollutionLog, pollutionIndexName):
        """pickleファイルに保存されている濃度分布リストを三次元リストに変換する"""

        #x, y, zの値の幅を調べる
        xSize, ySize, zSize, _ = pollutionLog.max()

        #pickleデータから、x, y, zの幅に応じたリストを生成
        xSize, ySize, zSize = int(xSize + 1), int(ySize + 1), int(zSize + 1)
        pollutionData = [[[0 for z in range(zSize)] for y in range(ySize)] for x in range(xSize)]

        #pickleデータの濃度リストは1次元なので3次元に変換
        count = 0
        for x_i in range(xSize):
            for y_i in range(ySize):
                for z_i in range(zSize):
                    pollutionData[x_i][y_i][z_i] = pollutionLog[str(pollutionIndexName)][count]
                    count += 1

        return pollutionData
