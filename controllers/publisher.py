from tkinter import *

class PublisherController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.buttonAdd["command"] = self.addDataToLbx
        self.view.buttonUpdate["command"] = self.updateDataFromLBX
        self.view.buttonRemove["command"] = self.removeDataFromLBX
        self.view.listbox.bind('<<ListboxSelect>>', self.loadLbxDataToEntry)
        self.loadDataToLBX()

    def loadDataToLBX(self):
        data = self.model.getAllData()
        self.view.setListbox(data)

    def addDataToLbx(self):
        self.addToDB()
        self.loadDataToLBX()

    def removeDataFromLBX(self):
        self.removeDataFromDB()
        self.loadDataToLBX()

    def updateDataFromLBX(self):
        self.updateDB()
        self.loadDataToLBX()

    def loadLbxDataToEntry(self, event=None):
        pub_name = self.view.getCursorPubName()
        pub_address = self.view.getCursorPubAddress()
        pub_phone = self.view.getCursorPubPhone()
        self.view.setPubName(pub_name)
        self.view.setPubAddress(pub_address)
        self.view.setPubPhone(pub_phone)
        print("ID: ", self.view.getCursorID(), "\nName: ", pub_name, "\nAdderess: ", pub_address, "\nPhone: ", pub_phone)

    def addToDB(self):
        pub_name    = self.view.getPubNameData()
        pub_address = self.view.getPubAddressData()
        pub_phone   = self.view.getPubPhoneData()
        self.model.addToTable(pub_name, pub_address,pub_phone)

    def updateDB(self):
        id = self.view.getCursorID()
        pub_name = self.view.getPubNameData()
        pub_address = self.view.getPubAddressData()
        pub_phone = self.view.getPubPhoneData()
        self.model.updateTable(id, pub_name, pub_address,pub_phone)

    def removeDataFromDB(self):
        id = self.view.getCursorID()
        self.model.deleteDataFromTable(id)