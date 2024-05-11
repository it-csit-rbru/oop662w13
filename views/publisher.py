from tkinter import *
class PublisherView:
    def __init__(self, root):
        self.root = root
        self.root.title("Publisher Table")
        self.createWidgets()

    def createWidgets(self):
        self.labelPubName = Label(self.root, text="Publisher Name: ")
        self.labelPubName.grid(row=0, column=0, padx=5, pady=5)

        self.entryPubNameTextVar = StringVar()
        self.entryPubName = Entry(self.root, textvariable=self.entryPubNameTextVar)
        self.entryPubName.grid(row=0, column=1, padx=5, pady=5)

        self.labelPubAddress = Label(self.root, text="Publisher Address: ")
        self.labelPubAddress.grid(row=1, column=0, padx=5, pady=5)

        self.entryPubAddressTextVar = StringVar()
        self.entryPubAddress = Entry(self.root, textvariable=self.entryPubAddressTextVar)
        self.entryPubAddress.grid(row=1, column=1, padx=5, pady=5)

        self.labelPubPhone = Label(self.root, text="Publisher Phone: ")
        self.labelPubPhone.grid(row=2, column=0, padx=5, pady=5)

        self.entryPubPhoneTextVar = StringVar()
        self.entryPubPhone = Entry(self.root, textvariable=self.entryPubPhoneTextVar)
        self.entryPubPhone.grid(row=2, column=1, padx=5, pady=5)
        
        self.buttonAdd = Button(self.root, text="Add")
        self.buttonAdd.grid(row=3, column=0, pady=5)

        self.buttonUpdate = Button(self.root, text="Update")
        self.buttonUpdate.grid(row=3, column=1, pady=5)

        self.buttonRemove = Button(self.root, text="Remove")
        self.buttonRemove.grid(row=3, column=2, pady=5)

        self.listbox = Listbox(self.root, width=60)
        self.listbox.grid(row=4, column=1, padx=5, pady=5)

    def getPubNameData(self):
        return self.entryPubNameTextVar.get()

    def getPubAddressData(self):
        return self.entryPubAddressTextVar.get()
    
    def getPubPhoneData(self):
        return self.entryPubPhoneTextVar.get()

    def setPubName(self, pub_name):
        self.entryPubNameTextVar.set(pub_name)

    def setPubAddress(self, pub_address):
        self.entryPubAddressTextVar.set(pub_address)

    def setPubPhone(self, pub_phone):
        self.entryPubPhoneTextVar.set(pub_phone)

    def getCursorID(self, event=None):
        selectedLbData = self.listbox.curselection()
        id = self.listbox.get(selectedLbData)[0]
        return id

    def getCursorPubName(self):
        selectedLbData = self.listbox.curselection()
        pub_name = self.listbox.get(selectedLbData)[1]
        return pub_name

    def getCursorPubAddress(self):
        selectedLbData = self.listbox.curselection()
        pub_address = self.listbox.get(selectedLbData)[2]
        return pub_address
    
    def getCursorPubPhone(self):
        selectedLbData = self.listbox.curselection()
        pub_phone = self.listbox.get(selectedLbData)[3]
        return pub_phone

    def setListbox(self, data):
        self.listbox.delete(0, END)
        for values in data:
            self.listbox.insert(END, values)