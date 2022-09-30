import os

current_path = os.getcwd()
current_path_result = current_path + "\\" +"result" + "\\"

def _result(filename):
    setDir(current_path_result)
    filename = Path_Check(filename)
    New_filename = current_path_result + filename
    return New_filename


def setDir(filepath):
    """
    判断目录中是否有该文件夹，若没有，就生成该文件夹。
    """
    if not os.path.exists(filepath):
        os.mkdir(filepath)
        
def Path_Check(path):
    """
    获取路径中文件名
    """
    return os.path.basename(path)
