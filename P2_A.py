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

#If the file is run directly, run the script
if __name__ == "__main__":
    main()
