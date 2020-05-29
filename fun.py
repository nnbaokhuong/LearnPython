#Add a list to dictionary

inventory = {
    'arrow' : 12,
    'gold coin' : 42,
    'rope' : 1,
    'torch' : 6,
    'dagger' : 1
    }
dragonLoot = ['gold coin','dagger','gold coin','ruby']

def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print(f'Total number of items: {total}') 

def addToInventory(inventory,addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] += 1

    return inventory

updatedInventory = addToInventory(inventory,dragonLoot)

displayInventory(updatedInventory)
