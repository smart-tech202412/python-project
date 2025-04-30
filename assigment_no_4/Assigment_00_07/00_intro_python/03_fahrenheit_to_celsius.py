def main():

    fahrenheit = float(input("\033[1;3 enter tempreature in fahrenheit: \033[0m"))

    celsius = (fahrenheit - 32) * 5.0/9.0

    print(f"tampreature : {fahrenheit}F = {celsius}C")

    if __name__=="__main__":
        main()