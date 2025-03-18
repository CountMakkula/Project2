import console_gfx
#Print the main menu
def Menu():
    print("RLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data\n")

def main():
    print("Welcome to the RLE image encoder!\n\nDisplaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    while True:
        Menu()
        Option = int(input("Select a Menu Option: "))
        #Exit
        if Option == 0:
            break
        #Load file
        elif Option == 1:
            FileName = input("Enter name of the file to load: ")
            ImageFile = console_gfx.load_file(FileName)
        #Load test image
        elif Option == 2:
            ImageFile = console_gfx.test_image
            print("Test image data loaded.")
        #Reads RLE string
        elif Option == 3:
            RLEString = input("Enter an RLE string to be decoded: ")
            ImageFile = decode_rle(string_to_rle(RLEString))
        #Reads RLE hex string
        elif Option == 4:
            RLEString = input("Enter the hex string holding RLE data: ")
            ImageFile = decode_rle(string_to_data(RLEString))
        #Reads RLE data in hex notation
        elif Option == 5:
            HexData = input("Enter the hex string holding flat data: ")
            ImageFile = []
            for i in HexData:
                ImageFile.append(HexIntConvert(i))
        #Displays the current image
        elif Option == 6:
            console_gfx.display_image(ImageFile)
        #Converts current data to human-readable RLE
        elif Option == 7:
            RLE = to_rle_string(encode_rle(ImageFile))
            print(f"RLE representation: {RLE}")
        #Converts current data to RLE hex
        elif Option == 8:
            RLE = to_hex_string(encode_rle(ImageFile))
            print(f"RLE hex values: {RLE}")
        #Displays current flat data in hex
        elif Option == 9:
            RLE = to_hex_string(ImageFile)
            print(f"Flat hex values: {RLE}")
        else:
            print("Error! Invalid input.")

#Translates RLE or raw data to a hexadecimal string
def to_hex_string(data):
    ReturnString = ""
    for val in data:
        ReturnString += str(HexIntConvert(val))
    return ReturnString

#Gives the number of runs of data in a set
def count_runs(flat_data):
    Runs = 0
    RunLength = 1
    for index, val in enumerate(flat_data):
        try:
            if flat_data[index+1] != flat_data[index]:
                Runs += 1
            else:
                RunLength += 1
                if RunLength == 15:
                    Runs += 1
                    RunLength = 0
        except:
            Runs += 1
    return Runs

#Encodes raw data to RLE
def encode_rle(flat_data):
    ReturnList = []
    RunLength = 1
    for index, val in enumerate(flat_data):
        try:
            if flat_data[index+1] == flat_data[index]:
                RunLength += 1
                if RunLength == 15:
                    RunLength = 0
                    ReturnList.append(15)
                    ReturnList.append(val)
            else:
                ReturnList.append(RunLength)
                ReturnList.append(val)
                RunLength = 1
        #If end of the flat data (next index is OoR), add the length and val of current run
        except:
            ReturnList.append(RunLength)
            ReturnList.append(val)
    return ReturnList

#Returns total number of runs
def get_decoded_length(rle_data):
    NumRuns = 0
    for index, val in enumerate(rle_data):
        if index % 2 == 0:
            NumRuns += val
    return NumRuns

#Decodes RLE to flat data
def decode_rle(rle_data):
    ReturnData = []
    for index, val in enumerate(rle_data):
        if index % 2 == 1:
            PrevVal = HexIntConvert(rle_data[index-1])
            for i in range(PrevVal):
                ReturnData.append(val)
    return ReturnData

#Translates hexadecimal string to RLE
def string_to_data(data_string):
    ReturnData = []
    for val in data_string:
        ReturnData.append(HexIntConvert(val))
    return ReturnData

#Translates RLE to a human-readable string
def to_rle_string(rle_data):
    ReturnStr = ""
    for index, val in enumerate(rle_data):
        if index % 2 == 0:
            ReturnStr += str(val)
        else:
            ReturnStr += (to_hex_string([val]) + ":")
    return ReturnStr[:-1]

#Translates human-readable string to RLE
def string_to_rle(rle_string):
    ReturnList = []
    RunAndVals = rle_string.split(":")
    for string in RunAndVals:
        ReturnList.append(int(string[:-1]))
        HexVal = string_to_data(string[-1])
        ReturnList.append(HexVal[0])
    return ReturnList

#Translates hex to int and vice versa
def HexIntConvert(val):
    try:
        IntValue = int(val)
        if IntValue == 10:
            return "a"
        elif IntValue == 11:
            return "b"
        elif IntValue == 12:
            return "c"
        elif IntValue == 13:
            return "d"
        elif IntValue == 14:
            return "e"
        elif IntValue == 15:
            return "f"
        else:
            return IntValue
    except:
        if val.lower() == "a":
            return 10
        elif val.lower() == "b":
            return 11
        elif val.lower() == "c":
            return 12
        elif val.lower() == "d":
            return 13
        elif val.lower() == "e":
            return 14
        elif val.lower() == "f":
            return 15

#If the file is run directly, run the script
if __name__ == "__main__":
    main()
