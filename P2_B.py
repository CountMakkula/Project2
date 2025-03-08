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
            FileName = input("Enter the name of the file: ")
            ImageFile = console_gfx.load_file(FileName)
        #Load test image
        elif Option == 2:
            ImageFile = console_gfx.test_image
            print("Test image data is loaded")
        elif Option == 6:
            console_gfx.display_image(ImageFile)
        else:
            print("Invalid selection")

#Translates RLE or raw data to a hexadecimal string
def to_hex_string(data):
    ReturnString = ""
    for val in data:
        if val < 10:
            ReturnString += str(val)
        elif val == 10:
            ReturnString += "a"
        elif val == 11:
            ReturnString += "b"
        elif val == 12:
            ReturnString += "c"
        elif val == 13:
            ReturnString += "d"
        elif val == 14:
            ReturnString += "e"
        elif val == 15:
            ReturnString += "f"
    return ReturnString

#Gives the number of runs of data in a set
def count_runs(flat_data):
    Runs = 0
    for index, val in enumerate(flat_data):
        try:
            if flat_data[index+1] != flat_data[index]:
                Runs += 1
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
            for i in range(rle_data[index-1]):
                ReturnData.append(val)
    return ReturnData

#Translates hexadecimal string to RLE
def string_to_data(data_string):
    ReturnData = []
    for val in data_string:
        if val == "a":
            ReturnData.append(10)
        if val == "b":
            ReturnData.append(11)
        if val == "c":
            ReturnData.append(12)
        if val == "d":
            ReturnData.append(13)
        if val == "e":
            ReturnData.append(14)
        if val == "f":
            ReturnData.append(15)
        else:
            ReturnData.append(int(val))
    return ReturnData

#If the file is run directly, run the script
#if __name__ == "__main__":
    #main()
