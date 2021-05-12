#Brett Meirhofer 2036955
import datetime
from csv import reader
from csv import writer

class InventoryItem:
    def __init__(self):
        #A list or a list of dictionaries could be used here instead of multiple separate variables
        #but having them separate like this makes it easier to control which category of values
        #are written to each csv file
        #Additioningly I included ItemID as a variable in the object despite it also the key for the
        #first dictionary so that the refrence can be passed between dict's with different keys without
        #gimmicky code to prevent data loss
        self.ItemID = 0
        self.Manufacturer = "none"
        self.ItemType = "none"
        self.Price = 0
        self.ServiceDate = ""
        self.TrueServiceDate = datetime.datetime.now()
        self.Damaged = ""

    def PrintItem(self):
        return ("{}|{}|{}|${}".format(self.ItemID, self.Manufacturer, self.ItemType, self.Price))

    def IsValid(self):
        CurrentDate = datetime.datetime.now()
        if ThisItem.Damaged == "":

            DateList = ThisItem.ServiceDate.split("/")
            for Index in range(0, len(DateList)):
                DateList[Index] = int(DateList[Index])

            ItemDate = datetime.datetime(DateList[2], DateList[0], DateList[1])
            if CurrentDate <= ItemDate:
                ValidItems.append(ThisItem)
                return True

        return False



#Temporary dict for using ItemID to locate objects and assign values
#ItemID:InventoryItem
InventoryDict = {}

Manufacturers = set()
ItemTypes = set()





#Opens ManufacturerList.csv and extracts ItemID,Manufacturer Name, ItemType, and Damaged status
with open("ManufacturerList.csv", "r") as ManufacturerList:
    CSVReader = reader(ManufacturerList)
    for Row in CSVReader:
        CurrentItem = InventoryItem()
        InventoryDict[Row[0]] = CurrentItem
        CurrentItem.ItemID = Row[0]
        CurrentItem.Manufacturer = Row[1]
        CurrentItem.ItemType = Row[2]
        CurrentItem.Damaged = Row[3]

        #Adds manufacturers and item types to lists so they can be reused later
        Manufacturers.add(CurrentItem.Manufacturer)
        ItemTypes.add(CurrentItem.ItemType)




#Opens PriceList.csv and extracts Prices
with open("PriceList.csv", "r") as PriceList:
    CSVReader = reader(PriceList)
    for Row in CSVReader:
        InventoryDict[Row[0]].Price = Row[1]


#Opens ServiceDatesList.csv and extracts Service Dates
with open("ServiceDatesList.csv", "r") as InputServiceList:
    CSVReader = reader(InputServiceList)
    for Row in CSVReader:
        InventoryDict[Row[0]].ServiceDate = Row[1]


#Loops until the user enters q
Input = ""
while Input != "q":
    Input = input("Enter Manufacturer,ItemType (Press q to quit)\n")
    if Input != "q":
        ValidItem = True
        InputTerms = Input.split(",")
        CurrentManufacturer = ""
        CurrentItemType = ""

        #Check if a Manufacturer and ItemType can be found in the input
        for Term in InputTerms:
            if Term in Manufacturers:
                if CurrentManufacturer == "":
                    CurrentManufacturer = Term
                else:
                    ValidItem = False
                continue

            if Term in ItemTypes:
                if CurrentItemType == "":
                    CurrentItemType = Term
                else:
                    ValidItem = False
                continue


        ValidItems = []
        if CurrentManufacturer != "" and CurrentItemType != "":
            # Makes a list of items that fit the itemtype/manf and are valid
            for ThisItem in InventoryDict.values():
                if ThisItem.ItemType == CurrentItemType:
                    if ThisItem.Manufacturer == CurrentManufacturer:
                        if ThisItem.IsValid():
                            ValidItems.append(ThisItem)

            #if no items are found then the query fails
            if len(ValidItems) <= 0:
                ValidItem = False
            #if items are found then select the highest price one
            else:
                ValidItems.sort(key=lambda Item: Item.Price)
                FinalItem = ValidItems[0]


        else:
            ValidItem = False


        if ValidItem:
            print("Your item is: {}".format(FinalItem.PrintItem()))
            #Looks for the same item type from a different manf that is valid and prints it
            for ThisItem in InventoryDict.values():
                if ThisItem.ItemType == CurrentItemType and ThisItem.Manufacturer != CurrentManufacturer:
                    if ThisItem.IsValid():
                        print("You may, also, consider: ”{}".format(ThisItem.PrintItem()))
                        break
        else:
            print("No such item in inventory")



