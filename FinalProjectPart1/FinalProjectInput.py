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
        self.Damaged = False

#Temporary dict for using ItemID to locate objects and assign values
#ItemID:InventoryItem
InventoryDict = {}

#Used for writing a csv file for each item type
#ItemType:InventoryItemArray
ItemTypeDict = {}

#Used for writing PastServiceDateInventory.csv
ServiceList = []

#Used for writing DamagedInventory.csv
DamageList = []

#Used for FullInventory.csv file
FullInventoryList = []

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

        ItemTypeDict[Row[2]] = []


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


#Sorts FullInventoryList by manufacturer name and writes each InventoryItem in the list to FullInventory.csv
FullInventoryList = sorted(InventoryDict.values(), key=lambda Item: Item.Manufacturer)
with open("FullInventory.csv", "w", newline='') as InventoryFile:
    CSVWriter = writer(InventoryFile)
    for Item in FullInventoryList:
        DamageString = ""
        CSVWriter.writerow([Item.ItemID,Item.Manufacturer,
                            Item.ItemType,Item.Price,Item.ServiceDate,Item.Damaged])


#Adds Item Refs from FullInventoryList into appropriate lists
CurrentDate = datetime.datetime.now()
for Item in FullInventoryList:
    #Add Items to ItemTypeDict
    ItemTypeDict[Item.ItemType].append(Item)

    #Add Items to ServiceList if applicable
    DateList = Item.ServiceDate.split("/")
    for Index in range(0, len(DateList)):
        DateList[Index] = int(DateList[Index])
    ItemDate = datetime.datetime(DateList[2], DateList[0], DateList[1])
    if CurrentDate > ItemDate:
        Item.TrueServiceDate = ItemDate
        ServiceList.append(Item)

    #Add Items to DamagedList if applicable
    if Item.Damaged == "damaged":
        DamageList.append(Item)


#Writes an ItemList to ItemType.csv files
for ItemType,ItemList in ItemTypeDict.items():
    FileName = ItemType + ".csv"
    ItemList.sort(key=lambda Item: int(Item.ItemID))
    with open(FileName, "w", newline='') as ItemTypeFile:
        CSVWriter = writer(ItemTypeFile)
        for Item in ItemList:
            CSVWriter.writerow([Item.ItemID, Item.Manufacturer,
                                Item.Price, Item.ServiceDate, Item.Damaged])


#Writes items to PastServiceDateInventory.csv
with open("PastServiceDateInventory.csv", "w", newline='') as InventoryFile:
    CSVWriter = writer(InventoryFile)
    ServiceList.sort(key=lambda Item: Item.TrueServiceDate)
    for Item in ServiceList:
        CSVWriter.writerow([Item.ItemID, Item.Manufacturer,
                            Item.ItemType, Item.Price, Item.ServiceDate, Item.Damaged])


#Writes items to DamagedInventory.csv
with open("DamagedInventory.csv", "w", newline='') as InventoryFile:
    CSVWriter = writer(InventoryFile)
    DamageList.sort(key=lambda Item: int(Item.Price), reverse=True)
    for Item in DamageList:
        CSVWriter.writerow([Item.ItemID, Item.Manufacturer,
                            Item.ItemType, Item.Price, Item.ServiceDate])



