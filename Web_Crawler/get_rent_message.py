from urllib.request import urlopen
import re
import csv

def main():

    csvfile=open('Rent_Message.csv','w',newline='')
    writer=csv.writer(csvfile)
    writer.writerow(['Price','Postcode','Type_Property','Num_Bedroom','Num_Bathroom','Num_Carspace','Address'])
    ## Make urls list
    urls=['https://www.realestate.com.au/rent/in-perth+-+greater+region,+wa/list-{}'.format(str(i)) for i in range(1,100)]
    ## Enter webpage
    for i in range(len(urls)):
        print("Page:",i+1,"Start Analyzing")
        html=urlopen(urls[i]).read().decode('utf-8')
        ## evalue
        csv_price=price(html)
        csv_postcode=postcode(html)
        csv_type_property=type_property(html)
        csv_num_bedroom=num_bedroom(html)
        csv_num_bathroom=num_bathroom(html)
        csv_num_car_space=num_car_space(html)
        csv_get_address=get_address(html)
        ## find address of missing data
        empty_price=findEmptyrow(csv_price)
        empty_postcode=findEmptyrow(csv_postcode)
        empty_type_property=findEmptyrow(csv_type_property)
        empty_num_bedroom=findEmptyrow(csv_num_bedroom)
        empty_num_bathroom=findEmptyrow(csv_num_bathroom)
        empty_num_car_space=findEmptyrow(csv_num_car_space)
        empty_get_address=findEmptyrow(csv_get_address)
##         delete row which has missing data
        removed_same_list=list(sorted(set(empty_price+empty_postcode+empty_type_property+empty_num_bedroom+empty_num_bathroom+empty_num_car_space+empty_get_address)))
        print("POP list:",removed_same_list)
##        print(csv_price)
##        print(csv_postcode)
##        print(csv_type_property)
##        print(csv_num_bedroom)
##        print(csv_num_bathroom)
##        print(csv_num_car_space)
##        print(csv_get_address)
        if removed_same_list!=[]:
            for i in reversed(removed_same_list):
                csv_price.pop(i)
                csv_postcode.pop(i)
                csv_type_property.pop(i)
                csv_num_bedroom.pop(i)
                csv_num_bathroom.pop(i)
                csv_num_car_space.pop(i)
                csv_get_address.pop(i)
        ## print final result
        print(csv_price)
        print(csv_postcode)
        print(csv_type_property)
        print(csv_num_bedroom)
        print(csv_num_bathroom)
        print(csv_num_car_space)
        print(csv_get_address)
        csvfile
        data=zip(csv_price,csv_postcode,csv_type_property,csv_num_bedroom,csv_num_bathroom,csv_num_car_space,csv_get_address)
        writer.writerows(data)
        csvfile.close


## find missing data
def findEmptyrow(function):
    empty=[]
    for i in range(len(function)):
        if function[i]==' ':
            empty.append(i)
        elif function[i]==[]:
            empty.append(i)
    return empty

def price(page):
    priceTextReg=re.compile(r"priceText\">(.+?)<")
    priceText = re.findall(priceTextReg,page)
    price_20=priceText[0:20]
    price_20Text=[]
    price_20Reg=re.compile(r"(\d+\.*,*(\d)*)")
    for i in range(len(price_20)):
        stuff=re.findall(price_20Reg,price_20[i])
        if stuff!=[]:
            price_20Text.append(stuff[0][0])
        else:
            price_20Text.append(' ')
    return price_20Text

def postcode(page):
    address=get_address(page)
    postcodeReg=re.compile(r"[WA|wa|Wa|wA][ *](\d\d\d\d)")
    postcode_20=[]
    for i in range(len(address)):
        append=re.findall(postcodeReg,address[i])
        if append!=[]:
            postcode_20.append(append[0])
        else:
            postcode_20.append(append)
    return postcode_20[0:20]

def type_property(page):
    propertyReg=re.compile(r"<a href=['|\"|]/property-(.+?)-wa[a-zA-Z0-9-\s\"'\+ ]{5,50}class='detailsButton'")
    propertyText=re.findall(propertyReg,page)
    property_20=propertyText[0:20]
    return property_20

def num_bedroom(page):
    bedroomReg=re.compile(r"Bedrooms</span></dt> <dd>(\d+)</dd>")
    bedroomText=re.findall(bedroomReg,page)
    bedroom_20=bedroomText[0:20]
    return bedroom_20

def num_bathroom(page):
    bathroomReg=re.compile(r"Bathrooms</span></dt> <dd>(\d+)</dd>")
    bathroomText=re.findall(bathroomReg,page)
    bathroom_20=bathroomText[0:20]
    return bathroom_20

def num_car_space(page):
    carspaceReg=re.compile(r"Car Spaces</span></dt> <dd>(\d+)</dd>")
    carspaceText=re.findall(carspaceReg,page)
    carspace_20=carspaceText[0:20]
    return carspace_20

def get_address(page):
    addressReg=re.compile(r"listingName'>(.+?)</a></h2></div>")
    addressText=re.findall(addressReg,page)
    address_20=addressText[0:20]
    return address_20

main()