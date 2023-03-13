import sys
import os
from PySide2 import *
from qt_material import *
#import PSUtil
import psutil
import PySide2extn
#import GPUtil
from multiprocessing import cpu_count
from datetime import *
import platform
import shutil
from time import sleep
import traceback

#GUI FILE
from ui_interface import *
##############################

#GLOBAL
platforms = {'linux':'Linux',
             'linux1':'Linux',
             'linux2':'Linux',
             'darwin':'OS X',
             'win32':'Windows'}
###########################################

###############################################################
#WORKER SIGNAL CLASS
class WorkerSignals(QObject):
    '''
    Define the signals available from a runing worker thread
        
        supported signals are:
        
    finished
        no data
            
    errror
        tuple(exctyoe,value,traceback.format_ecv())
            
    result
        object data returned from processing, anything
        
    progress
        int indicating % progress
            
    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
################################################################################

##################################################################################
#WORKER CLASS
class Worker(QRunnable):
    '''
    worked thread
    
    Inherits from QRunnable to handler worker thread setup,signals and wrap-up
    
    :params callback: the function callback to run on this worker thread.
    Supplied args and
                     Kwargs will be passed through to the runner.
    
    :type callback: the function
    :params args: Argumnmets to pass to the callback function.
    :params kwargs: Keyword to pass to the callback function.
    '''
    
    def __init__(self,fn,*args,**kwargs):
        super(Worker,self).__init__()
        
        #store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
        #add the callback to our kwargs
        self.kwargs['progress_callbaack'] = self.signals.progress
    
    @Slot()
    def run(self):
        #Initialise the runner function with passed args,kwargs
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args,**self.kwargs)
        except:
            traceback.print_exc()
            exctype,value = sys.exc_info((exctype,value,traceback.format_exc()))
        else:
            self.signals.result.emit(result) #return the result
        finally:
            self.signals.finished.emit() #Done

##########################################################################################################




###################################
#Main window class
class MainWindow(QMainWindow):
    def __init__(self): #setup stylesheet
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #load style sheet 
        apply_stylesheet(app,theme='dark_cyan.xml')
        #Remove window bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        #set main window transparent
        self.setAttribute(Qt.WA_TranslucentBackground)
        #shadow effect styke
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,550))
        #apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        #set icon window
        self.setWindowIcon(QIcon("C:/Users/Jose Luis/OneDrive/Escritorio/Moni_App/icon/feather/airplay-32x32-433956.png"))
        self.setWindowTitle("UTIL MANAGER")
        #Window size grip to resize window
        QSizeGrip(self.ui.size_grip)
        #Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda:
            self.showMinimized())
        #Close Window
        self.ui.close_window_button.clicked.connect(lambda:
            self.close())
        #Restore window
        self.ui.restore_window_button.clicked.connect(lambda:
            self.restore_or_maximize_window())
        
        ##############################################
        #Stacked Pages navigation
        #Using butttons
        ###############################################
        
        #cpu page
        self.ui.cpu_btn.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_memory))
        #battery page
        self.ui.battery_btn.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentWidget(self.ui.battery))
        #sys info page
        self.ui.system_info_btn.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentWidget(self.ui.system_information))
        #activties page
        self.ui.activity_btn.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentWidget(self.ui.activities))
        #Storage page
        self.ui.storage_btn.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
        #sensors page
        self.ui.sensors_page_btn.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))
        #network page
        self.ui.networks_page_btn.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentWidget(self.ui.networks))
        ##############################################################################
        ######################################################################################
        
        #Function to move window on mouse drag event on the title bar
        #############################################################
        def moveWindow(e):
            if self.isMaximized() == False: #not maximized
                #move window only when window is normal size
                ############################################
                # if left button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    #move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        ##########################################################################
        # add click event/mouse move event/drag event to the top header to move window
        self.ui.header_frame.mouseMoveEvent = moveWindow
        ##############################################################################
        
        #left menu toggle button (show hide mwnu labels)
        self.ui.open_close_side_bar_btn.clicked.connect(lambda:self.slideLeftMenu())
        #######################################################################################
        
        ########################################################################################
        #style clicked button menu button
        for w in self.ui.menu_frame.findChildren(QPushButton):
            #Add click event listener
            w.clicked.connect(self.applyButtonStyle)
        ##########################################################################################
        
        self.threadpool = QThreadPool()
        
        self.show()
        #self.battery()
        #self.cpu_ram()
        self.system_info()
        self.processes()
        self.storage()
        self.networks()
        self.psutil_thread()
    
    ###################################################################################################
    #CREATE A PSUTIL THREAD FUNCTION
    def psutil_thread(self):
        worker = Worker(self.cpu_ram)
        
        #start workers
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        
        #Execute
        self.threadpool.start(worker)
    #######################################################################################################
    
    #######################################################################################################
    #WORKER PRINT_OUT
    def print_output(self,s):
        print(s)
    ##########################################################################################################
    
    ################################################################################################################
    #WORKER THREAD COMPLETE FUNCTION
    def thread_complete(self):
        print("THREAD COMPLETE")
    ############################################################################################################
    
    #######################################################################################################################
    #WORKER THREAD PROGRESS FUNCTION
    def progress_fn(self,n):
        print("%d% done"  % n)
    
    ####################################################################################################
    # NETWORK INFORMATION
    def networks(self):
        #NET STATS
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()
            #Create New Row
            rowPosition = self.ui.net_stats_table.rowCount()
            self.ui.net_stats_table.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition,0,x,"net_stats_table")
            self.create_table_widget(rowPosition,1,str(z[x].isup),"net_stats_table")
            self.create_table_widget(rowPosition,2,str(z[x].duplex),"net_stats_table")
            self.create_table_widget(rowPosition,3,str(z[x].speed),"net_stats_table")
            self.create_table_widget(rowPosition,4,str(z[x].mtu),"net_stats_table")
            
        #NET IO COUNTERS
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)
            #create new row
            
            rowPosition = self.ui.net_io_table.rowCount()
            self.ui.net_io_table.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition,0,x,"net_io_table")
            self.create_table_widget(rowPosition,1,str(z[x].bytes_sent),"net_io_table")
            self.create_table_widget(rowPosition,2,str(z[x].bytes_recv),"net_io_table")
            self.create_table_widget(rowPosition,3,str(z[x].packets_sent),"net_io_table")  
            self.create_table_widget(rowPosition,4,str(z[x].packets_recv),"net_io_table")
            self.create_table_widget(rowPosition,5,str(z[x].errin),"net_io_table")
            self.create_table_widget(rowPosition,6,str(z[x].errout),"net_io_table")
            self.create_table_widget(rowPosition,7,str(z[x].dropin),"net_io_table")
            self.create_table_widget(rowPosition,8,str(z[x].dropout),"net_io_table")
        
        #NET ADDRESSES
        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()
            #print z
            for y in z[x]:
                #create a new row
                rowPosition = self.ui.net_addresses_table.rowCount()
                self.ui.net_addresses_table.insertRow(rowPosition)
                
                self.create_table_widget(rowPosition,0,str(x),"net_addresses_table")
                self.create_table_widget(rowPosition,1,str(y.family),"net_addresses_table")
                self.create_table_widget(rowPosition,2,str(y.address),"net_addresses_table")
                self.create_table_widget(rowPosition,3,str(y.netmask),"net_addresses_table")
                self.create_table_widget(rowPosition,4,str(y.broadcast),"net_addresses_table")
                self.create_table_widget(rowPosition,5,str(y.ptp),"net_addresses_table")
                
        #NET CONNECTIONS
        for x in psutil.net_connections():
            z = psutil.net_connections()
            #create new row
            rowPosition = self.ui.net_connections_table.rowCount()
            self.ui.net_connections_table.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition,0,str(x.fd),"net_connections_table")
            self.create_table_widget(rowPosition,1,str(x.family),"net_connections_table")
            self.create_table_widget(rowPosition,2,str(x.type),"net_connections_table")
            self.create_table_widget(rowPosition,3,str(x.laddr),"net_connections_table")
            self.create_table_widget(rowPosition,4,str(x.raddr),"net_connections_table")
            self.create_table_widget(rowPosition,5,str(x.status),"net_connections_table")
            self.create_table_widget(rowPosition,6,str(x.pid),"net_connections_table")        
    ####################################################################################################
    
    
    
    
    #####################################################################################################
    #STORAGE PARTITIONS
    def storage(self):
        global platforms
        storage_device = psutil.disk_partitions(all=False)
        z = 0
        for x in storage_device:
            #print(x)
            #Create a new row
            rowPosition = self.ui.storage_table.rowCount()
            self.ui.storage_table.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition,0,x.device,"storage_table")
            self.create_table_widget(rowPosition,1,x.mountpoint,"storage_table")
            self.create_table_widget(rowPosition,2,x.fstype,"storage_table")
            self.create_table_widget(rowPosition,3,x.opts,"storage_table")
            
            if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
                self.create_table_widget(rowPosition,4,str(x.maxfile))
                self.create_table_widget(rowPosition,5,str(x.maxpath))
            else:
                self.create_table_widget(rowPosition,4,"Function not available on" + platforms[sys.platform],"storage_table")
                self.create_table_widget(rowPosition,5,"Function not available on" + platforms[sys.platform],"storage_table")
            
            disk_usage = shutil.disk_usage(x.mountpoint)
            #print(disk_usage.total)
            self.create_table_widget(rowPosition,6,str((disk_usage.total / (1024 * 1024 * 1024))) + " GB","storage_table")
            self.create_table_widget(rowPosition,8,str((disk_usage.free / (1024 * 1024 * 1024))) + " GB","storage_table")
            self.create_table_widget(rowPosition,7,str((disk_usage.used / (1024 * 1024 * 1024))) + " GB","storage_table")
            #print(psutil.disk_usage(x.mountpoint))
            
            full_disk = (disk_usage.used / disk_usage.total) * 100
            progressBar = QProgressBar(self.ui.storage_table)
            progressBar.setObjectName(u"progressBar")
            progressBar.setValue(full_disk)
            self.ui.storage_table.setCellWidget(rowPosition,9,progressBar)
    ##############################################################################################################################################            
                
                
            
            
        
    ############################################################################################
    #FUNCTION TO CREATE THAT TABLE WIDGETS
    def create_table_widget(self,rowPosition,columPosition,text,tableName):
       qtablewidgetitem = QTableWidgetItem()
       getattr(self.ui, tableName).setItem(rowPosition,columPosition,qtablewidgetitem)
       qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition,columPosition)
       qtablewidgetitem.setText(text);
    ##############################################################################################
        
    ##############################################################################################
    # RUNNING PROCESSES
    def processes(self):
        for x in psutil.pids():
            #create new row
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            
            try:
                process = psutil.Process(x)
                # create widget
                #print(process)
                # rowPosition = row number
                #x = column number
                self.create_table_widget(rowPosition, 0, str(process.pid),"tableWidget")
                self.create_table_widget(rowPosition, 1, str(process.name()),"tableWidget")
                self.create_table_widget(rowPosition, 2, str(process.status()),"tableWidget")
                self.create_table_widget(rowPosition, 3, str(datetime.utcfromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')),"tableWidget")
                
                #create an all widget
                suspend_btn = QPushButton(self.ui.tableWidget)
                suspend_btn.setText('Suspend')
                suspend_btn.setStyleSheet("color: brown")
                self.ui.tableWidget.setCellWidget(rowPosition,4,suspend_btn)
                
                resume_btn = QPushButton(self.ui.tableWidget)
                resume_btn.setText('Resume')
                resume_btn.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition,5,resume_btn)
                
                termite_btn = QPushButton(self.ui.tableWidget)
                termite_btn.setText('Termite')
                termite_btn.setStyleSheet("color: orange")
                self.ui.tableWidget.setCellWidget(rowPosition,6,termite_btn)
                
                kill_btn = QPushButton(self.ui.tableWidget)
                kill_btn.setText('Kill')
                kill_btn.setStyleSheet("color: red")
                self.ui.tableWidget.setCellWidget(rowPosition,7,kill_btn)
            except Exception as e:
                print(e)
        
        self.ui.activity_search.textChanged.connect(self.findName)
        
    ################################################################################################    
    #SEARCH ACTIVITY TABLE
    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row,1)
            # if the search is not in the item's text do not hide the row
            self.ui.tableWidget.setRowHidden(row,name not in item.text().lower())
    ###############################################################################################            
                
                
    ################################################################################################    
    #GET SYTEM INFORMATION
    def system_info(self):
        time = datetime.now().strftime("%I:%M%S %p")
        self.ui.system_date.setText(str(time))
        date = datetime.now().strftime("%Y-%m-%d")
        self.ui.system_time.setText(str(date))
        
        self.ui.machine.setText(platform.machine())
        self.ui.version.setText(platform.version())
        self.ui.platform.setText(platform.platform())
        self.ui.systemy_information.setText(platform.system())
        self.ui.processor.setText(platform.processor())
    #####################################################################################################    
    
    #SYSTEM CPU AND RAM INFORMATION
    def cpu_ram(self,progress_callbaack):
        while True:
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam / (1024 * 1024 *1024)
            self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + ' GB'))
            
            availRam = 1.0
            availRam = psutil.virtual_memory()[1] * availRam
            availRam = availRam / (1024 * 1024 *1024)
            self.ui.available_ram.setText(str("{:.4f}".format(availRam) + ' GB'))
            
            ramUsed = 1.0
            ramUsed = psutil.virtual_memory()[3] * ramUsed
            ramUsed = ramUsed / (1024 * 1024 *1024)
            self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + ' GB'))
            
            ramFree = 1.0
            ramFree = psutil.virtual_memory()[4] * ramUsed
            ramFree = ramFree / (1024 * 1024 *1024)
            self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + ' GB'))
            
            ramUsages = str(psutil.virtual_memory()[2]) + ' %'
            self.ui.usage_ram.setText(str("{:.4f}".format(totalRam) + ' GB'))
            
            core = cpu_count()
            self.ui.cpu_count.setText(str(core))
            
            
            cpuPer = psutil.cpu_percent(interval=1)
            self.ui.cpu_per.setText(str(cpuPer) + ' %')
            cpuMainCore = psutil.cpu_count(logical=False)
            self.ui.cpu_main.setText(str(cpuMainCore))
            
            #cpu percentage indicator
            #set progress bar value
            self.ui.cpu_usage.rpb_setMaximum(100)
            # set progress values
            self.ui.cpu_usage.rpb_setValue(cpuPer)
            #set progress bar style
            self.ui.cpu_usage.rpb_setBarStyle('Hybrid2')
            #set progress bar line color
            self.ui.cpu_usage.rpb_setLineColor((255,30,99))
            #set bar line color
            #self.ui.cpu_usage.rpb_setCircleColor((45,74,83))
            #set progress bar line color
            self.ui.cpu_usage.rpb_setPieColor((45,74,83))
            #changing the path color
            #self.ui.cpu_usage.rpb_setPathColor((45,74,83))
            #set progress bar text color
            self.ui.cpu_usage.rpb_setTextColor((255,255,255))
            #set progress bar starting position
            # North,West,East,South
            self.ui.cpu_usage.rpb_setInitialPos('West')
            #set progress bar text type: value or percentage
            self.ui.cpu_usage.rpb_setTextFormat('Percentage')
            
            #set progress bar font
            self.ui.cpu_usage.rpb_setTextFont('Arial')
            #text hiddem
            #self.ui.cpu_usage.rpb_enableText(False)
            #set progress bar line width
            self.ui.cpu_usage.rpb_setLineWidth(15)
            #path width
            self.ui.cpu_usage.rpb_setPathWidth(15)
            #set progress bar line cap
            self.ui.cpu_usage.rpb_setLineCap('RoundCap')
            #self.ui.cpu_usage.rpb_setLineStyle('DashLine')
            
            #Ram usage spiral bar
            #setting the minimun value
            self.ui.ram_usage.spb_setMinimum((0,0,0))
            #settin maximum value
            self.ui.ram_usage.spb_setMaximum((totalRam,totalRam,totalRam))
            #set progress value
            self.ui.ram_usage.spb_setValue((availRam,ramUsed,ramFree))
            #set progress color r.g,b
            self.ui.ram_usage.spb_lineColor(((6,233,38),(6,201,233),(233,6,201)))
            # set initial position of the progress bar outer-> inwards
            self.ui.ram_usage.spb_setInitialPos(('West','West','West'))
            #set line width
            self.ui.ram_usage.spb_lineWidth(15)
            #set gap width
            self.ui.ram_usage.spb_setGap(15)
            #set line style
            self.ui.ram_usage.spb_lineStyle(('SolidLine','SolidLine','SolidLine'))
            #set line cap
            self.ui.ram_usage.spb_lineCap(('RoundCap','RoundCap','RoundCap'))
            #hide the path
            self.ui.ram_usage.spb_setPathHidden(True)
            #SLEPP
            sleep(1)
        ##############################################################################################################
        
        
        

        
        
        
        
        
        
        
    ################################################################################################
    # get system battery information
    ################################################################################################
    '''def battery(self):
        batt = psutil.sensors_battery()
        
        
        
        if not hasattr(psutil,"sensors_battery"):
            self.ui.battery_status.setText("Platform not supported")
        
        if batt is None:
            self.ui.battery_status.setText("No battery installed")
        
        if batt.power_plugged:
            self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
            self.ui.battery_time_left.setText("N/A")

            if batt.percent < 100:
                self.ui.battery_status.setText("Charging")
            else:
                self.ui.battery_status.setText("Fully Charged")
            self.ui.battery_plugged.setText("Yes")
        else:
            self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
            self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))
            if batt.percent < 100:
                self.ui.battery_status.setText("Discharging")
            else:
                self.ui.battery_status.setText("Fully Charged")
            self.ui.battery_plugged.setText("No")
        
        #battery power indicator using around progress bar
        #set progress bar valus
        self.ui.battery_usage.rpb_setMaximum(100)
        #set progress values
        self.ui.battery_usage.rpb_setValue(batt.percent)
        #set bar style
        self.ui.battery_usage.rpb_setBarStyle('Hybrid2')
        #set progress bar line color
        self.ui.battery_usage.rpb_setLineColor((255,30,99))
        #set progress bar line color
        #self.ui.battery_usage.rpb.setCircleColor((45,74,83))
        #set progress bar line color
        self.ui.battery_usage.rpb_setPieColor((45,74,83))
        #Changing the path color
        #set progress bar line color.rpb_setPathColor((45,74,83))
        #set bar text color
        self.ui.battery_usage.rpb_setTextColor((255,255,255))
        #set progress bar starting position
        #North,East,West,South
        self.ui.battery_usage.rpb_setInitialPos('West')
        #set progress bar text type: value or percentage
        #value, percentage
        self.ui.battery_usage.rpb_setTextFormat('Percentage')
        #set progress bar font
        #set progress bar line width
        self.ui.battery_usage.rpb_setLineWidth(15)
        #path width
        self.ui.battery_usage.rpb_setPathWidth(15)
        #set progress bar line cap
        # roundcap, squarecap
        self.ui.battery_usage.rpb_setLineCap('RoundCap')
        #line style
        #Dot line Dash line
        #self.ui.battery_usage.rpb_setLineStyle('DotLine')
    ###########################################################################################################################'''
    
           
    ###################################################################################################
    #side menu buttons styling fucntions
    ####################################################################################################
    def applyButtonStyle(self):
        #reset style for other buttons
        for w in self.ui.menu_frame.findChildren(QPushButton):
            #if button name is not equal to clicked button name
            if w.objectName() != self.sender().objectName():
                #create defautl style  by removing the left border
                #lets remove the bottom border style
                #lets also remove the left border style
                #aply the default style
                w.setStyleSheet("border-bottom: none;")
            #Apply new style to clicekd button
            #sender = clicked button
            #get the clicked button stylesheet then add new left-border style to it
            #lets add the bottom borer style
            #apply the new style
            self.sender().setStyleSheet("border-bottom: 2px solid")
            return
    
    
    
    ##############################################################################
    #slide menu function left
    ##############################################################################
    def slideLeftMenu(self):
        #get currrent left menu width
        width = self.ui.left_menu_count_frame.width()
        
        #if minimized
        if width == 60:
            #expan menu
            newWidth = 200
        else:
            #restore menu
            newWidth = 60
        #animated menu
        self.animation = QPropertyAnimation(self.ui.left_menu_count_frame,b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        
    ####################################################################
    #add mouse event to the window
    ####################################################################
    def mousePressEvent(self, event):
        #get current position of the mouse
        self.clickPosition = event.globalPos() 
        #we will use this value to move the window 
    #####################################################################
    
        
    ##############################################################
    #Update restore button icon on maximize or minizing window
    #################################################################
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QIcon(u"icon/feather/chevron-32x32-433998.png"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QIcon(u"icon/feather/chevron-32x32-433998.png"))
###################################################
#Execute App
#####################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =  MainWindow()
    sys.exit(app.exec_())