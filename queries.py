from connection import MySQLConnection
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLineEdit, QComboBox, QStatusBar, QTableWidget, QTableWidgetItem

# 1
def design_add_airplane(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    self.airline = QLabel("airlineID")
    self.airline.setFixedWidth(50)
    combobox1 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM airline")
            result = cursor.fetchall()
    
    for tuple in result:
        combobox1.addItem(tuple['airlineID'])
    # combobox1.addItem('One')
    # combobox1.addItem('Two')
    # combobox1.addItem('Three')
    # combobox1.addItem('Four')
    tailnum_box = QLineEdit()
    tailnum_box.setFixedWidth(80)
    # def update_tail_num():
    #     with MySQLConnection() as conn:
    #         with conn.cursor() as cursor:
    #             print("airlineID is " + str(combobox1.currentText()))
    #             cursor.execute("SELECT * FROM airplane WHERE airlineID = '" + str(combobox1.currentText()) + "'")
    #             result = cursor.fetchall()
    #             print("result = " + str(result))
    #     self.combobox2.clear()
    #     for tuple in result:
    #         self.combobox2.addItem(tuple['tail_num'])


    # combobox1.currentIndexChanged.connect(update_tail_num)

    combobox1.setFixedWidth(80)
    hbox1.addWidget(self.airline)
    hbox1.addWidget(combobox1)
    self.route_id_button= QLabel("plane_type")
    self.route_id_button.setFixedWidth(70)
    plane_type = QLineEdit()
    plane_type.setFixedWidth(200)
    hbox1.addWidget(self.route_id_button)
    hbox1.addWidget(plane_type)

    hbox2 = QHBoxLayout()
    self.tailnum = QLabel("tailnum")
    self.tailnum.setFixedWidth(50)

    hbox2.addWidget(self.tailnum)
    hbox2.addWidget(tailnum_box)
    self.tailnum2= QLabel("skids")
    self.tailnum2.setFixedWidth(40)
    skids = QLineEdit()
    skids.setFixedWidth(200)
    hbox2.addWidget(self.tailnum2)
    hbox2.addWidget(skids)

    hbox3 = QHBoxLayout()
    self.seat_capacity = QLabel("seat_capacity")
    seat_capacity1 = QLineEdit()
    hbox3.addWidget(self.seat_capacity)
    hbox3.addWidget(seat_capacity1)

    self.propeller = QLabel("propeller")
    propeller1 = QLineEdit()
    hbox3.addWidget(self.propeller)
    hbox3.addWidget(propeller1)

    hbox4 = QHBoxLayout()
    self.speed = QLabel("speed")
    speed1 = QLineEdit()
    hbox4.addWidget(self.speed)
    hbox4.addWidget(speed1)
    self.jet_engine = QLabel("jet_engine")
    jet_engine1= QLineEdit()
    hbox4.addWidget(self.jet_engine)
    hbox4.addWidget(jet_engine1)

    hbox5 = QHBoxLayout()
    self.locationID = QLabel("location_id")
    combobox3 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM location")
            result = cursor.fetchall()

    combobox3.addItem('')
    for tuple in result:
        combobox3.addItem(tuple['locationID'])

    hbox5.addWidget(self.locationID)
    hbox5.addWidget(combobox3)


    hbox6 = QHBoxLayout()
    self.cancel = QPushButton("cancel")
    self.cancel.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    self.add = QPushButton("add")
    def execute_add_airplane():
        print("I'm inside the function call")
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                print("selected seat capacity: " + seat_capacity1.text())
                sc = seat_capacity1.text()
                if sc == "":
                    sc = None

                s = speed1.text()
                if s == "":
                    s = None

                locID = combobox3.currentText()
                if locID == "":
                    locID = None

                pt = plane_type.text()
                if pt == "":
                    pt = None

                sk = skids.text()
                if sk == "":
                    sk = None

                prop = propeller1.text()
                if prop == "":
                    prop = None

                je = jet_engine1.text()
                if je == "":
                    je =  None

                cursor.callproc('add_airplane', args=(combobox1.currentText(), tailnum_box.text(), sc, s, locID, pt, sk, prop, je))
                conn.commit()

        tailnum_box.setText("")
        # print("I'm here with " + str(type(seat_capacity1)))
        seat_capacity1.setText("")
        speed1.setText("")
        plane_type.setText("")
        skids.setText("")
        propeller1.setText("")
        jet_engine1.setText("")

    self.add.clicked.connect(execute_add_airplane)
    hbox6.addWidget(self.cancel)
    hbox6.addWidget(self.add)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    vbox.addLayout(hbox4)
    vbox.addLayout(hbox5)
    vbox.addLayout(hbox6)
    self.add_airplane_page.setLayout(vbox)

# 2
def design_add_airport(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    hbox1.addWidget(QLabel("airportID")) 
    self.seat12 = QLineEdit()
    hbox1.addWidget(self.seat12)

    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("airport_name")) 
    self.seat22 = QLineEdit()
    hbox2.addWidget(self.seat22)

    hbox3 = QHBoxLayout()
    hbox3.addWidget(QLabel("City")) 
    self.seat32 = QLineEdit()
    hbox3.addWidget(self.seat32)

    hbox4 = QHBoxLayout()
    hbox4.addWidget(QLabel("State")) 
    self.seat42 = QLineEdit()
    hbox4.addWidget(self.seat42)

        
    hbox5 = QHBoxLayout()
    hbox5.addWidget(QLabel("location_id"))
    combobox3 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM location")
            result = cursor.fetchall()
    combobox3.addItem("")
    for tuple in result:
        combobox3.addItem(tuple['locationID'])
    hbox5.addWidget(combobox3)

    hbox7 = QHBoxLayout()
    cancel10_button = QPushButton("Cancel")
    hbox7.addWidget(cancel10_button)
    cancel10_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    
    update10_button = QPushButton("Add")
    hbox7.addWidget(update10_button)

    def call_add_airport():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                locID = combobox3.currentText()
                if locID == "":
                    locID = None
                cursor.callproc('add_airport', args=(self.seat12.text(), self.seat22.text(), self.seat32.text(), self.seat42.text(), locID))
                conn.commit()
        self.word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Airport add was successful!', 5000)
    update10_button.clicked.connect(call_add_airport)


    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    vbox.addLayout(hbox4)
    vbox.addLayout(hbox5)
    vbox.addLayout(hbox7)
    self.add_airport_page.setLayout(vbox)

# 3
def design_add_person(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    self.personID = QLabel("personID")
    self.personID.setFixedWidth(75)
    person_id_entry = QLineEdit()
    hbox1.addWidget(self.personID)
    hbox1.addWidget(person_id_entry)
    self.route_id_button= QLabel("experience")
    self.plane_type = QLineEdit()
    hbox1.addWidget(self.route_id_button)
    hbox1.addWidget(self.plane_type)
    hbox2 = QHBoxLayout()
    self.tailnum= QLabel("first_name")
    first_name_var = QLineEdit()
    hbox2.addWidget(self.tailnum)
    hbox2.addWidget(first_name_var)
    self.tailnum2= QLabel("airline")
    self.plane_type1 = QLineEdit()
    hbox2.addWidget(self.tailnum2)
    hbox2.addWidget(self.plane_type1)
    hbox3 = QHBoxLayout()
    self.seat_capacity = QLabel("last_name")
    seat_capacity1 = QLineEdit()
    hbox3.addWidget(self.seat_capacity)
    hbox3.addWidget(seat_capacity1)
    self.propeller = QLabel("tail")
    self.propeller1 = QLineEdit()
    hbox3.addWidget(self.propeller)
    hbox3.addWidget(self.propeller1)

    hbox4 = QHBoxLayout()
    self.speed = QLabel("taxID")
    self.speed1 = QLineEdit()
    hbox4.addWidget(self.speed)
    hbox4.addWidget(self.speed1)
    self.jet_engine = QLabel("miles")
    self.jet_engine1= QLineEdit()
    hbox4.addWidget(self.jet_engine)
    hbox4.addWidget(self.jet_engine1)

    hbox5 = QHBoxLayout()
    self.locationID = QLabel("location_id")
    combobox3 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT locationID FROM location")
            result = cursor.fetchall()
    for tuple in result:
        combobox3.addItem(tuple['locationID'])
    hbox5.addWidget(self.locationID)
    hbox5.addWidget(combobox3)


    hbox6 = QHBoxLayout()
    cancel3_button = QPushButton("Cancel")
    hbox6.addWidget(cancel3_button)
    cancel3_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    self.add = QPushButton("add")
    def execute_add_person():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                # print("selected routeID: " + word_entry.text())
                r = self.speed1.text()
                if r == "":
                    r = None

                a = self.plane_type.text()
                if a == "":
                    a = None

                b = self.plane_type1.text()
                if b == "":
                    b = None

                c = self.propeller1.text()
                if c == "":
                    c = None

                d = self.jet_engine1.text()
                if d == "":
                    d = None

                cursor.callproc('add_person', args=(person_id_entry.text(), first_name_var.text(), seat_capacity1.text(), combobox3.currentText(), r, a, b, c, d))
                conn.commit()
        #enter_flight_id.setText("")
        #enter_route_id.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Person Added Successfully!', 5000)
    self.add.clicked.connect(execute_add_person)
    hbox6.addWidget(self.add)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    vbox.addLayout(hbox4)
    vbox.addLayout(hbox5)
    vbox.addLayout(hbox6)
    self.add_person_page.setLayout(vbox)

# 4
def design_grant_pilot_license(self):
    vbox = QVBoxLayout()
    hbox1 = QHBoxLayout()
    combobox1 = QComboBox()
    hbox1.addWidget(QLabel("personID"))
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT personID FROM person")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['personID'])
    hbox1.addWidget(combobox1)

    hbox2 = QHBoxLayout()
    combobox2 = QComboBox()
    hbox2.addWidget(QLabel("license"))
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT distinct license FROM pilot_licenses")
            result = cursor.fetchall()
    for tuple in result:
        combobox2.addItem(tuple['license'])
    hbox2.addWidget(combobox2)


    hbox3 = QHBoxLayout()
    cancel4_button = QPushButton("Cancel")
    cancel4_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    hbox3.addWidget(cancel4_button)
    grant_button = QPushButton("Grant")
    hbox3.addWidget(grant_button)
    def call_grant_pilot_license():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('grant_pilot_license', args=(combobox1.currentText(), combobox2.currentText()))
                conn.commit()
        self.word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Pilot License Added successfully!', 5000)
    grant_button.clicked.connect(call_grant_pilot_license)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    self.grant_pilot_license_page.setLayout(vbox)

# 5
def design_offer_flight(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    self.airline = QLabel("flightID")
    enter_flight_id = QLineEdit()
    hbox1.addWidget(self.airline)
    hbox1.addWidget(enter_flight_id)
    self.route_id_button= QLabel("support_tail")
    self.plane_type1 = QLineEdit()
    hbox1.addWidget(self.route_id_button)
    hbox1.addWidget(self.plane_type1)

    hbox2 = QHBoxLayout()
    self.tailnum= QLabel("routeID")
    enter_route_id = QLineEdit()
    hbox2.addWidget(self.tailnum)
    hbox2.addWidget(enter_route_id)
    self.tailnum2= QLabel("progress")
    self.plane_type2 = QLineEdit()
    hbox2.addWidget(self.tailnum2)
    hbox2.addWidget(self.plane_type2)

    hbox3 = QHBoxLayout()
    self.seat_capacity = QLabel("support_airline")
    combobox1 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT airlineID FROM airline")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['airlineID'])
    hbox3.addWidget(self.seat_capacity)
    hbox3.addWidget(combobox1)
    self.propeller = QLabel("airplane_status")
    combobox2 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT distinct airplane_status FROM flight")
            result = cursor.fetchall()
    for tuple in result:
        combobox2.addItem(tuple['airplane_status'])
    hbox3.addWidget(self.propeller)
    hbox3.addWidget(combobox2)

    hbox4 = QHBoxLayout()
    self.next_time = QLabel("Next Time")
    self.entry1 = QLineEdit("")
    hbox4.addWidget(self.next_time)
    hbox4.addWidget(self.entry1)

    hbox5 = QHBoxLayout()
    cancel5_button = QPushButton("Cancel")
    hbox5.addWidget(cancel5_button)
    cancel5_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    self.add = QPushButton("add")
    def execute_offer_flight():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                # print("selected routeID: " + word_entry.text())
                st = self.plane_type1.text()
                if st == "":
                    st = None

                p = self.plane_type2.text()
                if p == "":
                    p = None

                q = self.entry1.text()
                if q == "":
                    q = None

                cursor.callproc('offer_flight', args=(enter_flight_id.text(), enter_route_id.text(), combobox1.currentText(), st, int(p), combobox2.currentText(), q))
                conn.commit()
        enter_flight_id.setText("")
        enter_route_id.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Flight offered successfully!', 5000)
    self.add.clicked.connect(execute_offer_flight)
    hbox5.addWidget(self.add)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    vbox.addLayout(hbox4)
    vbox.addLayout(hbox5)
    self.offer_flight_page.setLayout(vbox)

# 6
def design_purchase_ticket_and_seat(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    hbox1.addWidget(QLabel("ticketID")) 
    seat1 = QLineEdit()
    hbox1.addWidget(seat1)

    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("Cost"))
    self.seat_capacity1 = QLineEdit()
    hbox2.addWidget(self.seat_capacity1)

    hbox3 = QHBoxLayout()
    hbox3.addWidget(QLabel("carrier"))
    self.seat_capacity2 = QLineEdit()
    hbox3.addWidget(self.seat_capacity2)

    hbox4 = QHBoxLayout()
    hbox4.addWidget(QLabel("customer"))
    self.seat_capacity3 = QLineEdit()
    hbox4.addWidget(self.seat_capacity3)

    hbox5 = QHBoxLayout()
    hbox5.addWidget(QLabel("deplane_at"))
    combobox3 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM airport")
            result = cursor.fetchall()
    
    for tuple in result:
        combobox3.addItem(tuple['airportID'])
    hbox5.addWidget(combobox3)

    hbox6 = QHBoxLayout()
    hbox6.addWidget(QLabel("seatnumber"))
    self.seat_capacity4 = QLineEdit()
    hbox6.addWidget(self.seat_capacity4)

    hbox7 = QHBoxLayout()
    cancel10_button = QPushButton("Cancel")
    hbox7.addWidget(cancel10_button)
    cancel10_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    
    update10_button = QPushButton("Update")
    hbox7.addWidget(update10_button)

    def execute_purchase_ticket_and_seat():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('purchase_ticket_and_seat', args=(seat1.text(), self.seat_capacity1.text(), self.seat_capacity2.text(), self.seat_capacity3.text(), combobox3.currentText(), self.seat_capacity4.text()))
                conn.commit()
        self.seat_capacity1.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Ticket purchased successfully!', 5000)
    update10_button.clicked.connect(execute_purchase_ticket_and_seat)


    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    vbox.addLayout(hbox4)
    vbox.addLayout(hbox5)
    vbox.addLayout(hbox6)
    vbox.addLayout(hbox7)
    self.purchase_ticket_and_seat_page.setLayout(vbox)

# 7
def design_add_update_leg(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    hbox1.addWidget(QLabel("legID")) 
    self.seat1 = QLineEdit()
    hbox1.addWidget(self.seat1)

    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("Distance")) 
    self.seat2 = QLineEdit()
    hbox2.addWidget(self.seat2)
        
    hbox5 = QHBoxLayout()
    hbox5.addWidget(QLabel("Departure"))
    combobox3 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM airport")
            result = cursor.fetchall()
    
    for tuple in result:
        combobox3.addItem(tuple['airportID'])
    hbox5.addWidget(combobox3)

    hbox6 = QHBoxLayout()
    hbox6.addWidget(QLabel("Arrival"))
    combobox4 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM airport")
            result = cursor.fetchall()
    
    for tuple in result:
        combobox4.addItem(tuple['airportID'])
    hbox6.addWidget(combobox4)

    hbox7 = QHBoxLayout()
    cancel10_button = QPushButton("Cancel")
    hbox7.addWidget(cancel10_button)
    cancel10_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    
    update10_button = QPushButton("Assign")
    hbox7.addWidget(update10_button)

    def execute_add_update_leg():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('add_update_leg', args=(self.seat1.text(), self.seat2.text(), combobox3.currentText(), combobox4.currentText()))
                conn.commit()
        self.word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Leg change/add was successful!', 5000)
    update10_button.clicked.connect(execute_add_update_leg)


    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox5)
    vbox.addLayout(hbox6)
    vbox.addLayout(hbox7)
    self.add_update_leg_page.setLayout(vbox)

# 8
def design_start_route(self):
    vbox = QVBoxLayout()
    hbox1 = QHBoxLayout()
    hbox1.addWidget(QLabel("routeID"))
    word_entry = QLineEdit()
    hbox1.addWidget(word_entry)
    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("legID"))
    combobox1 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT legID FROM leg")
            result = cursor.fetchall()
    
    for tuple in result:
        combobox1.addItem(tuple['legID'])
    hbox2.addWidget(combobox1)

    hbox3 = QHBoxLayout()
    cancel8_button = QPushButton("Cancel")
    hbox3.addWidget(cancel8_button)
    cancel8_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    assign8_button = QPushButton("Assign")
    hbox3.addWidget(assign8_button)
    def call_start_route():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                # print("selected routeID: " + word_entry.text())
                cursor.callproc('start_route', args=(word_entry.text(), combobox1.currentText()))
                conn.commit()
        word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Route started successfully!', 5000)
    assign8_button.clicked.connect(call_start_route)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)

    self.start_route_page.setLayout(vbox)

# 9
def design_extend_route(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    hbox1.addWidget(QLabel("routeID"))
    word_entry = QLineEdit()
    hbox1.addWidget(word_entry)

    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("legID"))

    combobox1 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT legID FROM leg")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['legID'])
    hbox2.addWidget(combobox1)

    hbox3 = QHBoxLayout()

    cancel9_button = QPushButton("Cancel")
    hbox3.addWidget(cancel9_button)
    cancel9_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    assign9_button = QPushButton("Assign")
    hbox3.addWidget(assign9_button)
    def call_extend_route():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('extend_route', args=(word_entry.text(), combobox1.currentText()))
                conn.commit()
        word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Route extended successfully!', 5000)
    assign9_button.clicked.connect(call_extend_route)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)

    self.extend_route_page.setLayout(vbox)

# 10
def design_flight_landing(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    hbox1.addWidget(QPushButton("flightID"))
    word_entry = QLineEdit()
    hbox1.addWidget(word_entry)

    hbox2 = QHBoxLayout()
    cancel10_button = QPushButton("Cancel")
    hbox2.addWidget(cancel10_button)
    cancel10_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    
    update10_button = QPushButton("Update")
    hbox2.addWidget(update10_button)
    def call_flight_landing():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('flight_landing', args=(word_entry.text(),))
                conn.commit()
        self.word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Flight landed successfully!', 5000)
    update10_button.clicked.connect(call_flight_landing)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)

    self.flight_landing_page.setLayout(vbox)

# 11
def design_flight_takeoff(self):
    vbox = QVBoxLayout()
    hbox1 = QHBoxLayout()
    hbox1.addWidget(QPushButton("flightID"))
    word_entry = QLineEdit()
    hbox1.addWidget(word_entry)
    hbox2 = QHBoxLayout()
    cancel11_button = QPushButton("Cancel")
    hbox2.addWidget(cancel11_button)
    cancel11_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    self.update_button = QPushButton("Update")
    def call_flight_takeoff():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('flight_takeoff', args=(word_entry.text(),))
                conn.commit()
        self.word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Flight took off successfully!', 5000)
    self.update_button.clicked.connect(call_flight_takeoff)
    hbox2.addWidget(self.update_button)
    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    self.flight_takeoff_page.setLayout(vbox)

# 12
def design_passengers_board(self):
    vbox = QVBoxLayout()
    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("flightID"))
    combobox1 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT flightID FROM flight")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['flightID'])
    hbox2.addWidget(combobox1)
    hbox3 = QHBoxLayout()
    cancel12_button = QPushButton("Cancel")
    hbox3.addWidget(cancel12_button)
    cancel12_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    continue12_button = QPushButton("Continue")
    hbox3.addWidget(continue12_button)
    def call_passengers_board():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('passengers_board', args=(combobox1.currentText(),))
                conn.commit()
        self.word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Passengers Boarded successfully!', 5000)
    continue12_button.clicked.connect(call_passengers_board)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    self.passengers_board_page.setLayout(vbox)

# 13
def design_passengers_disembark(self):
    vbox = QVBoxLayout()
    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("flightID"))
    combobox1 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT flightID FROM flight")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['flightID'])
    hbox2.addWidget(combobox1)
    hbox3 = QHBoxLayout()
    cancel13_button = QPushButton("Cancel")
    hbox3.addWidget(cancel13_button)
    cancel13_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    continue13_button = QPushButton("Continue")
    hbox3.addWidget(continue13_button)
    def call_passengers_disembark():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('passengers_disembark', args=(combobox1.currentText(),))
                conn.commit()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Passengers Disembarked successfully!', 5000)
    continue13_button.clicked.connect(call_passengers_disembark)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    self.passengers_disembark_page.setLayout(vbox)

# 14
def design_assign_pilot(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    
    hbox1.addWidget(QLabel('personID'))
   
    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("Flight"))

    combobox1 = QComboBox()

    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT personID FROM person")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['personID'])

    hbox1.addWidget(combobox1)

    combobox2 = QComboBox()

    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT flightID FROM flight")
            result1 = cursor.fetchall()
    for tuple in result1:
        combobox2.addItem(tuple['flightID'])

    hbox2.addWidget(combobox2)

    hbox3 = QHBoxLayout()

    cancel14_button = QPushButton('Cancel')
    hbox3.addWidget(cancel14_button)
    cancel14_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    assign14_button = QPushButton('Assign')
    hbox3.addWidget(assign14_button)
    def call_assign_pilot():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('assign_pilot', args=(combobox2.currentText(), combobox1.currentText()))
                conn.commit()

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Pilot assigned successfully!', 5000)
    assign14_button.clicked.connect(call_assign_pilot)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
        
    self.assign_pilot_page.setLayout(vbox)

# 15
def design_recycle_crew(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    
    hbox1.addWidget(QLabel('Flight'))

    combobox1 = QComboBox()

    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT flightID FROM flight")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['flightID'])

    hbox1.addWidget(combobox1)

    hbox3 = QHBoxLayout()

    cancel14_button = QPushButton('Cancel')
    hbox3.addWidget(cancel14_button)
    cancel14_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    assign14_button = QPushButton('Recycle Crew')
    hbox3.addWidget(assign14_button)
    def call_recycle_crew():
        with MySQLConnection() as conn:
            
            with conn.cursor() as cursor:
                
                
                setup1 = "update flight set progress = 3 where flightID = 'AM_1523';"
                setup2 = "update person set locationID = 'port_5' where personID in ('p26', 'p40', 'p41');"
                cursor.execute(setup1)
                cursor.execute(setup2)
                #result = cursor.fetchall()
                cursor.callproc('recycle_crew', args=(combobox1.currentText(),))
                conn.commit()

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Crew Recycled!', 5000)
    assign14_button.clicked.connect(call_recycle_crew)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox3)
        
    self.recycle_crew_page.setLayout(vbox)

# 16
def design_retire_flight(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    
    hbox1.addWidget(QLabel("flightID"))
    self.word_entry = QLineEdit()
    hbox1.addWidget(self.word_entry)

    hbox3 = QHBoxLayout()

    cancel14_button = QPushButton('Cancel')
    hbox3.addWidget(cancel14_button)
    cancel14_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    assign14_button = QPushButton('Update')
    hbox3.addWidget(assign14_button)
    def call_retire_flight():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('retire_flight', args=(self.word_entry.text(),))
                conn.commit()
        self.word_entry.setText("")
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Flight Retired!', 5000)
    assign14_button.clicked.connect(call_retire_flight)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox3)
        
    self.retire_flight_page.setLayout(vbox)

# 17
def design_remove_passenger_role(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    
    hbox1.addWidget(QLabel("personID"))

    combobox1 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT personID FROM passenger")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['personID'])
    hbox1.addWidget(combobox1)

    hbox3 = QHBoxLayout()

    cancel14_button = QPushButton('Cancel')
    hbox3.addWidget(cancel14_button)
    cancel14_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    assign14_button = QPushButton('Remove')
    hbox3.addWidget(assign14_button)
    def call_remove_passenger_role():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('remove_passenger_role', args=(combobox1.currentText(),))
                conn.commit()

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Passenger Removed!', 5000)
    assign14_button.clicked.connect(call_remove_passenger_role)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox3)
        
    self.remove_passenger_role_page.setLayout(vbox)

# 18
def design_remove_pilot_role(self):
    vbox = QVBoxLayout()

    hbox1 = QHBoxLayout()
    
    hbox1.addWidget(QLabel("personID"))

    combobox1 = QComboBox()
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT personID FROM pilot")
            result = cursor.fetchall()
    for tuple in result:
        combobox1.addItem(tuple['personID'])
    hbox1.addWidget(combobox1)

    hbox3 = QHBoxLayout()

    cancel14_button = QPushButton('Cancel')
    hbox3.addWidget(cancel14_button)
    cancel14_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    assign14_button = QPushButton('Remove Pilot')
    hbox3.addWidget(assign14_button)
    def call_remove_pilot_role():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('remove_pilot_role', args=(combobox1.currentText(),))
                conn.commit()

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Pilot Removed!', 5000)
    assign14_button.clicked.connect(call_remove_pilot_role)

    vbox.addLayout(hbox1)
    vbox.addLayout(hbox3)
        
    self.remove_pilot_role_page.setLayout(vbox)

# 19
def design_flights_in_the_air(self):
    def check_table(testTable):
        num_rows = testTable.rowCount()
        print("num_rows = " + str(num_rows))
        num_cols = testTable.columnCount()
        print("num_cols = " + str(num_cols))
        

        # Update the values in the table
        for row in range(num_rows):
            for col in range(num_cols):
                item = testTable.item(row, col)
                if item is not None:
                    print(str(item.text()) + ", ", end="")
                else:
                    print("NULL, ", end="")
            print("", end="\n")

    departure_pushbutton = QPushButton("Sort Departure Airport in Ascending Order")
    arrival_pushbutton = QPushButton("Sort Arrival Airport in Ascending Order")
    earliest_arrival_pushbutton = QPushButton("Sort Earliest Arrival in Ascending Order")
    latest_arrival_pushbutton = QPushButton("Sort Latest Arrival in Ascending Order")
    go_back_pushbutton = QPushButton("Go Back to the Main Screen")

    vbox = QVBoxLayout()
    vbox.addWidget(departure_pushbutton)
    vbox.addWidget(arrival_pushbutton)
    vbox.addWidget(earliest_arrival_pushbutton)
    vbox.addWidget(latest_arrival_pushbutton)
    
    table = QTableWidget()
    vbox.addWidget(table)

    def CreateTable(self, result, oldTable):
        oldTable.setRowCount(len(result))
        oldTable.setColumnCount(7)
        oldTable.setHorizontalHeaderLabels(["Departure Airport", "Arrival Airport", "Number Flights", "Flight List", "Earliest Arrival", "Latest Arrival", "Airplane List"])
        oldTable.setColumnWidth(0, 150)

        for i, data in enumerate(result):
            oldTable.setItem(i, 0, QTableWidgetItem(data['departing_from']))
            oldTable.setItem(i, 1, QTableWidgetItem(data['arriving_at']))
            oldTable.setItem(i, 2, QTableWidgetItem(str(data['num_flights'])))
            oldTable.setItem(i, 3, QTableWidgetItem(data['flight_list']))
            oldTable.setItem(i, 4, QTableWidgetItem(str(data['earliest_arrival'])))
            oldTable.setItem(i, 5, QTableWidgetItem(str(data['latest_arrival'])))
            oldTable.setItem(i, 6, QTableWidgetItem(data['airplane_list']))
                
        # print("Here's the table after modfication insdie CreateTable:")
        # check_table(oldTable)

        # check_table(vbox.itemAt(4).widget())
    
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM flights_in_the_air")
            result = cursor.fetchall()
            # print("result = " + str(result))

    CreateTable(self, result, table)
    # print("here's the table after initialization:")
    # check_table(table)

    vbox.addWidget(go_back_pushbutton)
    
    def change_depart_text():
        if departure_pushbutton.text() == "Sort Departure Airport in Ascending Order":
            departure_pushbutton.setText("Sort Departure Airport in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_in_the_air ORDER BY departing_from ASC")
                    result = cursor.fetchall()
            # check_table(table)
            CreateTable(self, result, table)
        else:
            departure_pushbutton.setText("Sort Departure Airport in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_in_the_air ORDER BY departing_from DESC")
                    result = cursor.fetchall()
            # check_table(table)
            CreateTable(self, result, table)

    def change_arrival_text():
        if arrival_pushbutton.text() == "Sort Arrival Airport in Ascending Order":
            arrival_pushbutton.setText("Sort Arrival Airport in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_in_the_air ORDER BY arriving_at ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            arrival_pushbutton.setText("Sort Arrival Airport in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_in_the_air ORDER BY arriving_at DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)

    def change_earliest_text():
        if earliest_arrival_pushbutton.text() == "Sort Earliest Arrival in Ascending Order":
            earliest_arrival_pushbutton.setText("Sort Earliest Arrival in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_in_the_air ORDER BY earliest_arrival ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            earliest_arrival_pushbutton.setText("Sort Earliest Arrival in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_in_the_air ORDER BY earliest_arrival DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
    
    def change_latest_text():
        if latest_arrival_pushbutton.text() == "Sort Latest Arrival in Ascending Order":
            latest_arrival_pushbutton.setText("Sort Latest Arrival in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_in_the_air ORDER BY latest_arrival ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            latest_arrival_pushbutton.setText("Sort Latest Arrival in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_in_the_air ORDER BY latest_arrival DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)

    departure_pushbutton.clicked.connect(change_depart_text)
    arrival_pushbutton.clicked.connect(change_arrival_text)
    earliest_arrival_pushbutton.clicked.connect(change_earliest_text)
    latest_arrival_pushbutton.clicked.connect(change_latest_text)
    go_back_pushbutton.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    self.flights_in_the_air_page.setLayout(vbox)

# 20
def design_flights_on_the_ground(self):
    def check_table(testTable):
        num_rows = testTable.rowCount()
        print("num_rows = " + str(num_rows))
        num_cols = testTable.columnCount()
        print("num_cols = " + str(num_cols))
        

        # Update the values in the table
        for row in range(num_rows):
            for col in range(num_cols):
                item = testTable.item(row, col)
                if item is not None:
                    print(str(item.text()) + ", ", end="")
                else:
                    print("NULL, ", end="")
            print("", end="\n")
    
    departure_pushbutton = QPushButton("Sort Departure Airport in Ascending Order")
    arrival_pushbutton = QPushButton("Sort Number of Flights in Ascending Order")
    earliest_arrival_pushbutton = QPushButton("Sort Earliest Arrival in Ascending Order")
    latest_arrival_pushbutton = QPushButton("Sort Latest Arrival in Ascending Order")
    go_back_pushbutton = QPushButton("Go Back to the Main Screen")

    vbox = QVBoxLayout()
    vbox.addWidget(departure_pushbutton)
    vbox.addWidget(arrival_pushbutton)
    vbox.addWidget(earliest_arrival_pushbutton)
    vbox.addWidget(latest_arrival_pushbutton)

    table = QTableWidget()
    vbox.addWidget(table)

    def CreateTable(self, result, oldTable):
        oldTable.setRowCount(len(result))
        oldTable.setColumnCount(6)
        oldTable.setHorizontalHeaderLabels(["Departure Airport", "Number Flights", "Flight List", "Earliest Arrival", "Latest Arrival", "Airplane List"])
        oldTable.setColumnWidth(0, 150)
        
        for i, data in enumerate(result):
            oldTable.setItem(i, 0, QTableWidgetItem(data['departing_from']))
            oldTable.setItem(i, 1, QTableWidgetItem(str(data['num_flights'])))
            oldTable.setItem(i, 2, QTableWidgetItem(data['flight_list']))
            oldTable.setItem(i, 3, QTableWidgetItem(str(data['earliest_arrival'])))
            oldTable.setItem(i, 4, QTableWidgetItem(str(data['latest_arrival'])))
            oldTable.setItem(i, 5, QTableWidgetItem(data['airplane_list']))
        
        # self.vbox.replaceWidget(self.table, newTable)
        # self.table = newTable

    with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM flights_on_the_ground")
                result = cursor.fetchall()
    
    CreateTable(self, result, table)
    vbox.addWidget(go_back_pushbutton)

    def change_depart_text():
        if departure_pushbutton.text() == "Sort Departure Airport in Ascending Order":
            departure_pushbutton.setText("Sort Departure Airport in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_on_the_ground ORDER BY departing_from ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            departure_pushbutton.setText("Sort Departure Airport in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_on_the_ground ORDER BY departing_from DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)

    def change_arrival_text():
        if arrival_pushbutton.text() == "Sort Number of Flights in Ascending Order":
            arrival_pushbutton.setText("Sort Number of Flights in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_on_the_ground ORDER BY num_flights ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            arrival_pushbutton.setText("Sort Number of Flights in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_on_the_ground ORDER BY num_flights DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)

    def change_earliest_text():
        if earliest_arrival_pushbutton.text() == "Sort Earliest Arrival in Ascending Order":
            earliest_arrival_pushbutton.setText("Sort Earliest Arrival in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_on_the_ground ORDER BY earliest_arrival ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            earliest_arrival_pushbutton.setText("Sort Earliest Arrival in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_on_the_ground ORDER BY earliest_arrival DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)

    def change_latest_text():
        if latest_arrival_pushbutton.text() == "Sort Latest Arrival in Ascending Order":
            latest_arrival_pushbutton.setText("Sort Latest Arrival in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_on_the_ground ORDER BY latest_arrival ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            latest_arrival_pushbutton.setText("Sort Latest Arrival in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM flights_on_the_ground ORDER BY latest_arrival DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
    
    departure_pushbutton.clicked.connect(change_depart_text)
    arrival_pushbutton.clicked.connect(change_arrival_text)
    earliest_arrival_pushbutton.clicked.connect(change_earliest_text)
    latest_arrival_pushbutton.clicked.connect(change_latest_text)
    go_back_pushbutton.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    
    self.flights_on_the_ground_page.setLayout(vbox)

# 21
def design_people_in_the_air(self):
    self.vbox = QVBoxLayout()
    def CreateTable(self):
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM people_in_the_air")
                result = cursor.fetchall()

        self.table = QTableWidget()
        rowCount = len(result)
        self.table.setRowCount(rowCount)
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels(["departure", "arrival", "Airplane Count", "Airplane List", "Flight List", "Earliest Arrival", "Latest Arrival", "Pilot Count", "Passenger Count", "Person Count", "Person List"])
        # self.table.setItem(0,0, QTableWidgetItem("Oz"))
        # self.table.setItem(0,1, QTableWidgetItem("14"))
        # self.table.setItem(0, 2 , QTableWidgetItem("Male"))
        self.table.setColumnWidth(0, 150)
        
        for i, data in enumerate(result):
            self.table.setItem(i, 0, QTableWidgetItem(data['departing_from']))
            self.table.setItem(i, 1, QTableWidgetItem(data['arriving_at']))
            self.table.setItem(i, 2, QTableWidgetItem(str(data['num_airplanes'])))
            self.table.setItem(i, 3, QTableWidgetItem(data['airplane_list']))
            self.table.setItem(i, 4, QTableWidgetItem(data['flight_list']))
            self.table.setItem(i, 5, QTableWidgetItem(str(data['earliest_arrival'])))
            self.table.setItem(i, 6, QTableWidgetItem(str(data['latest_arrival'])))
            self.table.setItem(i, 7, QTableWidgetItem(str(data['num_pilots'])))
            self.table.setItem(i, 8, QTableWidgetItem(str(data['num_passengers'])))
            self.table.setItem(i, 9, QTableWidgetItem(str(data['joint_pilots_passengers'])))
            self.table.setItem(i, 10, QTableWidgetItem(data['person_list']))
    CreateTable(self)
    self.vbox.addWidget(self.table)
    go_back_pushbutton = QPushButton("Go Back to the Main Screen")
    self.vbox.addWidget(go_back_pushbutton)
    go_back_pushbutton.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    
    self.people_in_the_air_page.setLayout(self.vbox)

# 22
def design_people_on_the_ground(self):
    self.vbox = QVBoxLayout()
    def CreateTable(self):
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM people_on_the_ground")
                result = cursor.fetchall()

        self.table = QTableWidget()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["departure", "location", "airport_name", "city", "state", "pilot count", "passenger count", "people count", "Person List"])
        # self.table.setItem(0,0, QTableWidgetItem("Oz"))
        # self.table.setItem(0,1, QTableWidgetItem("14"))
        # self.table.setItem(0, 2 , QTableWidgetItem("Male"))
        self.table.setColumnWidth(0, 150)

        for i, data in enumerate(result):
            self.table.setItem(i, 0, QTableWidgetItem(data['departing_from']))
            self.table.setItem(i, 1, QTableWidgetItem(data['airport']))
            self.table.setItem(i, 2, QTableWidgetItem(data['airport_name']))
            self.table.setItem(i, 3, QTableWidgetItem(data['city']))
            self.table.setItem(i, 4, QTableWidgetItem(data['state']))
            self.table.setItem(i, 5, QTableWidgetItem(str(data['num_pilots'])))
            self.table.setItem(i, 6, QTableWidgetItem(str(data['num_passengers'])))
            self.table.setItem(i, 7, QTableWidgetItem(str(data['joint_pilots_passengers'])))
            self.table.setItem(i, 8, QTableWidgetItem(data['person_list']))
    CreateTable(self)
    self.vbox.addWidget(self.table)
    go_back_pushbutton = QPushButton("Go Back to the Main Screen")
    self.vbox.addWidget(go_back_pushbutton)
    go_back_pushbutton.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    self.people_on_the_ground_page.setLayout(self.vbox)

# 23
def design_route_summary(self):
    departure_pushbutton = QPushButton("Sort Route in Ascending Order")
    arrival_pushbutton = QPushButton("Sort Route Length in Ascending Order")
    go_back_pushbutton = QPushButton("Go Back to the Main Screen")

    vbox = QVBoxLayout()
    vbox.addWidget(departure_pushbutton)
    vbox.addWidget(arrival_pushbutton)

    table = QTableWidget()
    # print(type(self.table))
    vbox.addWidget(table)

    def CreateTable(self, result, oldTable):
        oldTable.setRowCount(len(result))
        oldTable.setColumnCount(7)
        oldTable.setHorizontalHeaderLabels(["Route", "Number of Legs", "Leg Sequence", "Route Length", "Number of Flights", "Flight List", "Airport Sequence"])
        oldTable.setColumnWidth(0, 150)
        
        for i, data in enumerate(result):
            oldTable.setItem(i, 0, QTableWidgetItem(data['route']))
            oldTable.setItem(i, 1, QTableWidgetItem(str(data['num_legs'])))
            oldTable.setItem(i, 2, QTableWidgetItem(data['leg_sequence']))
            oldTable.setItem(i, 3, QTableWidgetItem(str(data['route_length'])))
            oldTable.setItem(i, 4, QTableWidgetItem(str(data['num_flights'])))
            oldTable.setItem(i, 5, QTableWidgetItem(data['flight_list']))
            oldTable.setItem(i, 6, QTableWidgetItem(data['airport_sequence']))
        
        # print(type(self.table))
        # vbox.replaceWidget(self.table, newTable)
        # self.table = newTable
    
    with MySQLConnection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM route_summary")
            result = cursor.fetchall()

    CreateTable(self, result, table)
    vbox.addWidget(go_back_pushbutton)

    def change_depart_text(self):
        if departure_pushbutton.text() == "Sort Route in Ascending Order":
            departure_pushbutton.setText("Sort Route in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM route_summary ORDER BY route ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            departure_pushbutton.setText("Sort Route in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM route_summary ORDER BY route DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)

    def change_arrival_text(self):
        if arrival_pushbutton.text() == "Sort Route Length in Ascending Order":
            arrival_pushbutton.setText("Sort Route Length in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM route_summary ORDER BY route_length ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            arrival_pushbutton.setText("Sort Route Length in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM route_summary ORDER BY route_length DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
    
    arrival_pushbutton.clicked.connect(change_arrival_text)
    departure_pushbutton.clicked.connect(change_depart_text)
    go_back_pushbutton.clicked.connect(lambda: self.pages.setCurrentIndex(0))

    self.route_summary_page.setLayout(vbox)

# 24
def design_alternative_airports(self):
    departure_pushbutton = QPushButton("Sort City in Ascending Order")
    arrival_pushbutton = QPushButton("Sort State in Ascending Order")
    go_back_pushbutton = QPushButton("Go Back to the Main Screen")

    vbox = QVBoxLayout()
    vbox.addWidget(departure_pushbutton)
    vbox.addWidget(arrival_pushbutton)

    table = QTableWidget()
    vbox.addWidget(table)

    def CreateTable(self, result, oldTable):
        oldTable.setRowCount(len(result))
        oldTable.setColumnCount(5)
        oldTable.setHorizontalHeaderLabels(["City", "State", "Number of Airports", "Airport Code List", "Airport Name List"])
        # newTable.setItem(0,0, QTableWidgetItem("Oz"))
        # newTable.setItem(0,1, QTableWidgetItem("14"))
        # newTable.setItem(0, 2 , QTableWidgetItem("Male"))
        oldTable.setColumnWidth(0, 150)

        # result = [{'city': 'Anchorage', 'state': 'AK', 'num_of_airports': 2, 'airport_code_list': 
        # 'ANC, MRI', 'airport_name_list': 'Ted Stevens Anchorage International Airport, Merill Field', }, 
        # {'city': 'Chicago', 'state': 'IL', 'num_of_airports': 2, 'airport_code_list': 
        # 'MDW, ORD', 'airport_name_list': 'Chicago Midway International Airport, O_Hare International Airport', }]
        
        for i, data in enumerate(result):
            oldTable.setItem(i, 0, QTableWidgetItem(data['city']))
            oldTable.setItem(i, 1, QTableWidgetItem(data['state']))
            oldTable.setItem(i, 2, QTableWidgetItem(str(data['num_airports'])))
            oldTable.setItem(i, 3, QTableWidgetItem(data['airport_code_list']))
            oldTable.setItem(i, 4, QTableWidgetItem(data['airport_name_list']))
        
        # self.vbox.replaceWidget(self.table, newTable)
        # self.table = newTable
    
    with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM alternative_airports")
                result = cursor.fetchall()
    
    CreateTable(self, result, table)
    vbox.addWidget(go_back_pushbutton)
    
    def change_depart_text(self):
        if departure_pushbutton.text() == "Sort City in Ascending Order":
            departure_pushbutton.setText("Sort City in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM alternative_airports ORDER BY city ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            departure_pushbutton.setText("Sort City in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM alternative_airports ORDER BY city DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)

    def change_arrival_text(self):
        if arrival_pushbutton.text() == "Sort State in Ascending Order":
            arrival_pushbutton.setText("Sort State in Descending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM alternative_airports ORDER BY state ASC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
        else:
            arrival_pushbutton.setText("Sort State in Ascending Order")
            with MySQLConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM alternative_airports ORDER BY state DESC")
                    result = cursor.fetchall()
            CreateTable(self, result, table)
    
    departure_pushbutton.clicked.connect(change_depart_text)
    arrival_pushbutton.clicked.connect(change_arrival_text)
    go_back_pushbutton.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    
    self.alternative_airports_page.setLayout(vbox)

# 25
def design_simulation_cycle(self):
    vbox = QVBoxLayout()
    hbox3 = QHBoxLayout()
    cancel25_button = QPushButton("Cancel")
    hbox3.addWidget(cancel25_button)
    cancel25_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
    run25_button = QPushButton("Run")
    hbox3.addWidget(run25_button)
    def call_simulation_cycle():
        with MySQLConnection() as conn:
            with conn.cursor() as cursor:
                cursor.callproc('simulation_cycle', args=())
                conn.commit()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Simulation Ran Successfully!', 5000)
    run25_button.clicked.connect(call_simulation_cycle)
    vbox.addLayout(hbox3)
    self.simulation_cycle_page.setLayout(vbox)
