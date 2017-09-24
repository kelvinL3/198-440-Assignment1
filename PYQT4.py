import sys
from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)



class Ui_Form(object):

	name = "no name"
	matrix1 = []
	matrix2 = []
	score = -1
	font = QtGui.QFont("Times", 18, QtGui.QFont.Bold) 
	boardType = "Puzzle Board"
	timeToExecute = -1

	def __init__(self, name, matrix1, matrix2, score, timeToExecute):
		self.name = name
		self.matrix1 = matrix1
		self.matrix2 = matrix2
		self.score = score
		self.timeToExecute = timeToExecute

	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8(self.name))
		Form.resize(1500, 800) # whole window #length, height 
			# self.layoutWidget = QtGui.QWidget(Form)
			# self.layoutWidget.setGeometry(QtCore.QRect(400, 20, 258, 227)) #other button I dont need
			# self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
			# self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
			# self.verticalLayout.setMargin(0)
			# self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
			# self.textBrowser = QtGui.QTextBrowser(self.layoutWidget)
			# self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
			# self.verticalLayout.addWidget(self.textBrowser)
			# self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
			# self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
			# self.verticalLayout.addWidget(self.pushButton_3)
		
		#self.Voltage_Label[i].setFont(font)

		self.layoutWidget1 = QtGui.QWidget(Form)
		self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 720, 720))
		self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))


		self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))


		#BoardType
		self.labelBoardType = QtGui.QLabel()
		self.labelBoardType.setText(str(self.boardType))
		self.labelBoardType.setAlignment(QtCore.Qt.AlignLeft)
		self.labelBoardType.setFont(self.font)
		self.verticalLayout_2.addWidget(self.labelBoardType)


		self.tableView = QtGui.QTableWidget(self.layoutWidget1)
		self.tableView.setObjectName(_fromUtf8("tableView"))

		self.verticalLayout_2.addWidget(self.tableView)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

		self.pushButton = QtGui.QPushButton(self.layoutWidget1)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.horizontalLayout.addWidget(self.pushButton)
		#self.pushButton_4 = QtGui.QPushButton(self.layoutWidget1)
		#self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		#self.horizontalLayout.addWidget(self.pushButton_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout)

		#scoreLabel
		self.labelScore = QtGui.QLabel()
		
		self.labelScore.setAlignment(QtCore.Qt.AlignLeft)
		self.labelScore.setFont(self.font)
		self.verticalLayout_2.addWidget(self.labelScore)
		text = "Score: " + str(self.score)
		#timeToExecuteLabel
		if self.timeToExecute != -1:
			text = text + "\t\t" + "Time: " + str(self.timeToExecute)
		
		self.labelScore.setText(text)

		#self.pushButton_2 = QtGui.QPushButton(Form)
		#self.pushButton_2.setGeometry(QtCore.QRect(320, 320, 175, 27))
		#self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

		self.retranslateUi(Form)
		self.ShowMem(self.matrix1)
		self.layoutWidget1.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding))
		QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SwitchBoard)
		#QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tableView.reset)
			#QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot2)
		#QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser.clear)
			#QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot3)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate(self.name, self.name, None))
		#self.pushButton_3.setText(_translate("Form", "PushButton", None))
		self.pushButton.setText(_translate(self.name, "Show Corresponding Distance/Puzzle Board", None))
		#self.pushButton_4.setText(_translate("Form", "Generate Memory", None))
		#self.pushButton_2.setText(_translate("Form", "Clear", None))
	def ShowMem(self, matrix):
		self.tableView.setRowCount(len(matrix))
		self.tableView.setColumnCount(len(matrix[0]))
		for i, row in enumerate(matrix):
			self.tableView.setRowHeight(i,50)
			for j, val in enumerate(row):
				self.tableView.setItem(i,j,QtGui.QTableWidgetItem(str(val)))
				self.tableView.item(i,j).setBackground(QtGui.QColor(220,220,220))
				self.tableView.setColumnWidth(j,50)
				self.tableView.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
				self.tableView.item(i,j).setFont(self.font)

	def SwitchBoard(self):
		if self.boardType == "Puzzle Board":
			self.ShowMem(self.matrix2)
			self.boardType = "Distance Board"
			self.labelBoardType.setText(self.boardType)
		elif self.boardType == "Distance Board":
			self.ShowMem(self.matrix1)
			self.boardType = "Puzzle Board"
			self.labelBoardType.setText(self.boardType)

def drawMatrix(name, matrix1, matrix2, score=None, timeToExecute=-1):
	#Here is the matrix i want to show
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form(name, matrix1, matrix2, score, timeToExecute)
	ui.setupUi(Form)
	Form.show()
	app.exec_()
	Form.hide()