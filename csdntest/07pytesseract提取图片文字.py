from PIL import Image
import pytesseract
import easygui

path = easygui.fileopenbox()  # 选择文件对话框
text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')  # 识别文字
print(text)