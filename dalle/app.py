import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore
from Ui_dalle import Ui_MainWindow  # 假设你的UI文件名为dalle.ui
from qt_material import apply_stylesheet, list_themes
import requests
import os
from datetime import datetime, timedelta, timezone
import dotenv
import itertools

class MyWindow(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        apply_stylesheet(self.app, theme='dark_teal.xml', invert_secondary=False)
        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setting = {}
        self.init_ui()
        
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        print('init ui')
        self.ui.theme = 0
        self.ui.pushButton_gen.clicked.connect(self.push_button_clicked)
        self.ui.pushButton_figdir.clicked.connect(self.bt_showdir)
        self.ui.pushButton_theme.clicked.connect(self.bt_change_theme)
        self.ui.progressBar.setValue(0)
        self.setWindowIcon(QIcon('dalle/favicon.ico'))
        self.show()
        # load .ENV variables
        dotenv.load_dotenv()
        
    def push_button_clicked(self):
        # 按钮点击事件
        print('button clicked')
        self.ui.progressBar.setValue(0)
        print(self.ui.comboBox_imgsize.currentText())
        model_name = self.ui.comboBox_model.currentText()
        image_size = self.ui.comboBox_imgsize.currentText()
        self.ui.sub_system_info.append("正在创建请求，请耐心等待……")
        prompts = self.ui.textEdit.toPlainText()
        if len(prompts) == 0:
            self.ui.sub_system_info.append("提示词不能为空！")
            return
        try:
            self.ui.sub_system_info.append("当前prompts：{}, 正在生成图片，请耐心等待……".format(prompts))
            # 判断风格类型
            style_prompts_dict = {"默认": '', "科研": '学术论文配图,流程图', "素材": '背景透明,简洁', "动漫": '动漫', "图表": '图表,统计'}
            prompts = style_prompts_dict[self.ui.comboBox_style.currentText()] + ',' + prompts
            # 判断APIKEY
            base_url = self.ui.lineEdit_baseurl.text() if self.ui.lineEdit_baseurl.text().__len__()!=0 else os.getenv('BASE_URL')
            api_key = self.ui.lineEdit_apikey.text() if self.ui.lineEdit_apikey.text().__len__()!=0 else os.getenv('API_KEY')
            QApplication.processEvents()
            response = requests.post(
                base_url,
                headers={"Authorization": api_key},
                json={"model": model_name, "size": image_size, "prompt": prompts, "n": 1},
            )
            self.ui.progressBar.setValue(30)
            self.ui.sub_system_info.append("正在下载图像，请耐心等待……")
            QApplication.processEvents()
            response.raise_for_status()
            data = response.json()["data"]
            
            download_folder = r"figs"
            os.makedirs(download_folder, exist_ok=True)
            current_time = datetime.now(timezone.utc) + timedelta(hours=8)  # GMT+8
            current_time_str = current_time.strftime("%Y%m%d-%H%M%S")
            
            for i, image in enumerate(data):
                image_url = image["url"]
                file_name = current_time_str + f"-{str(i+1).zfill(3)}.png"
                file_path = self.download_image(image_url, download_folder)
                new_file_path = os.path.join(download_folder, file_name)
                os.rename(file_path, new_file_path)
                self.ui.sub_system_info.append("图片已下载至：{}".format(new_file_path))
                pixmap = QPixmap(new_file_path)
                self.ui.label.setPixmap(pixmap.scaled(self.ui.label.size()))
            self.ui.progressBar.setValue(100)
            QApplication.processEvents()
        except requests.exceptions.HTTPError as err:
            self.ui.sub_system_info.append("请求错误：{}".format(err.response.text))
            print(("请求错误：{}".format(err.response.text)))
        
        except Exception as e:
            self.ui.sub_system_info.append("发生错误：{}".format(str(e)))
            print("发生错误：{}".format(str(e)))
            
    def download_image(self, url, folder_path):
        response = requests.get(url)
        file_path = os.path.join(folder_path, os.path.basename(url))
        with open(file_path, "wb") as file:
            file.write(response.content)
        return file_path
    
    def bt_fileselect(self, param=''):
        # 选择文件
        self.ui.sub_system_info.clear()
        if param == 'figs_dir':
            default_dir = os.path.join(os.getcwd(), 'figs')
            file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", default_dir, "所有文件 (*)")
            # 如果用户选择了文件，则更新
            if file_path:
                print(file_path)
                self.ui.lineEdit.setText(file_path)
                self.ui.sub_system_info.append("数据路径更新成功！")
                return file_path
            else:
                print("未选择文件")
                return
        elif param == 'xx':
            
            return
    
    def bt_showdir(self):
        default_dir = os.path.join(os.getcwd(), 'figs')
        os.startfile(default_dir)
        return
    
    def bt_change_theme(self):
        # 切换主题
        self.ui.theme = self.ui.theme + 1 if self.ui.theme < len(list_themes()) - 1 else 0
        extra = {
            # Density Scale
            'density_scale': '0',
        }
        apply_stylesheet(self.app, theme=list_themes()[self.ui.theme], invert_secondary=False, extra=extra)
        # 如何在TextBrowser中显示不同色彩的文字：html语法
        # self.ui.sub_system_info.append("<font color='red'>Red Text</font><br>")
        # 如何通过按钮触发另一个窗口显示
        # dialog = Dialog()
        # dialog.exec_()
        return


class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dialog')
        self.setGeometry(300, 300, 200, 100)
        
        
# 程序入口
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    e = MyWindow()
    sys.exit(e.app.exec())