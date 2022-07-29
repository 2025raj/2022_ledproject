lblStorage = Label(DataFrameLeft, font=("arial", 12, "bold"),
                   text="Storage Advice:", padx=2, pady=6)
lblStorage.grid(row=2, column=2, sticky=W)
txtStorage = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
txtStorage.grid(row=2, column=3)


lblMedicine = Label(DataFrameLeft, font=(
    "arial", 12, "bold"), text="Medication", padx=2, pady=6)
lblMedicine.grid(row=3, column=2, sticky=W)
txtMedicine = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
txtMedicine.grid(row=3, column=3, sticky=W)


lblPatientId = Label(DataFrameLeft, font=(
    "arial", 12, "bold"), text="PatientId", padx=2, pady=6)
lblPatientId.grid(row=4, column=2, sticky=W)
txtPatientId = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
txtPatientId.grid(row=4, column=3)


lblNhsNumber = Label(DataFrameLeft, font=(
    "arial", 12, "bold"), text="NHS Number", padx=2, pady=6)
lblNhsNumber.grid(row=5, column=2, sticky=W)
txtNhsNumber = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
txtNhsNumber.grid(row=5, column=3)


lblPatientname = Label(DataFrameLeft, font=(
    "arial", 12, "bold"), text="Patient Name", padx=2, pady=6)
lblPatientname.grid(row=6, column=2, sticky=W)
txtPatientname = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
txtPatientname.grid(row=6, column=3)


lblDateOfBirth = Label(DataFrameLeft, font=(
    "arial", 12, "bold"), text="Date Of Birth", padx=2, pady=6)
lblDateOfBirth.grid(row=7, column=2, sticky=W)
txtDateOfBirth = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
txtDateOfBirth.grid(row=7, column=3)


lblPatientAddress = Label(DataFrameLeft, font=(
    "arial", 12, "bold"), text="Patient Address", padx=2, pady=6)
lblPatientAddress.grid(row=8, column=2, sticky=W)
txtPatientAddress = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
txtPatientAddress.grid(row=8, column=3)


#===========================    (DataframeRight)   =======================================#

self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"))
self.txtPrescription.grid(row=0, column=0)


#================    ( Buttons)    ===========================================================#


btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=(
    "arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
btnPrescription.grid(row=0, column=0)

btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=(
    "arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
btnPrescriptionData.grid(row=0, column=1)

btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=(
    "arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
btnUpdate.grid(row=0, column=2)

btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=(
    "arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
btnDelete.grid(row=0, column=3)

btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=(
    "arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
btnClear.grid(row=0, column=4)

btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=(
    "arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
btnExit.grid(row=0, column=5)


#==================================== ( Table ) ================================================================#

#==========================================  (  Scrollbar )  ============================================#

scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)

scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

self.hospital_table = ttk.Treeview(FrameDetails, column=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate",
                                   "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack = (side=BOTTOM, fill=X)
scroll_y.pack = (side=RIGHT, fill=Y)


scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

self.hospital_table.heading("nameoftable", text="Name of Table")
self.hospital_table.heading("ref", text="Reference No. ")
self.hospital_table.heading("dose", text="Dose")
self.hospital_table.heading("nooftablets", text="No Of Tablets")
self.hospital_table.heading("lot", text="Lot")
self.hospital_table.heading("issuedate", text="Issue Date")
self.hospital_table.heading("expdate", text="Exp Date")
self.hospital_table.heading("dailydose", text="Daily Dose")
self.hospital_table.heading("storage", text="Storage")
self.hospital_table.heading("nhsnumber", text="NHS Number")
self.hospital_table.heading("pname", text="Patient Name")
self.hospital_table.heading("dob", text="DOB")
self.hospital_table.heading("address", text="Address")


self.hospital_table["show"] = "headings"

self.hospital_table.column("nameoftable", width=100)
self.hospital_table.column("ref", width=100)
self.hospital_table.column("dose", width=100)
self.hospital_table.column("nooftablets", width=100)
self.hospital_table.column("lot", width=100)
self.hospital_table.column("issuedate", width=100)
self.hospital_table.column("expdate", width=100)
self.hospital_table.column("dailydose", width=100)
self.hospital_table.column("storage", width=100)
self.hospital_table.column("nhsnumber", width=100)
self.hospital_table.column("pname", width=100)
self.hospital_table.column("dob", width=100)
self.hospital_table.column("address", width=100)


self.hospital_table.pack(fill=BOTH, expand=1)
self.fatch_data()


# ===============  (Functionality Declaration) ====================#


def iPrescriptionData(self):
    if self.Nameoftablets.get() == "" or self.ref.get() = "":
        messagebox.showerror("Error", "All fields are required")
    else:
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Test@123", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

            self.Nameoftablets.get(),
            self.ref.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),

        ))

        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been inserted")


def fatch_data(self):
    conn = mysql.connector.connect(
        host="localhost", username="root", password="Test@123", database="Mydata")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from hospital")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        self.hospital_table.delete(*self.hospital_table.get_children())
        for i in rows:
            self.hospital_table.insert("", END, values=i)
        conn.commit()
    conn.close()
