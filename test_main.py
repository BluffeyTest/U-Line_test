#import wood as wd 
from test_myself import *
import sys
#wd.get_task()
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    #my_MainWindow = QMainWindow()
    #ui = my_MainWindow()
    Window=MainWindow()

    #ui.setupUi(MainWindow) 
    Window.show()
    sys.exit(app.exec_())