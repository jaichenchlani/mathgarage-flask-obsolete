def convert_decimal_to_binary(strInput):
    print("Entering convert_decimal_to_binary...")
    
    print("strInput:{}; Type of strInput:{}".format(strInput,type(strInput)))

    try:
        n = int(strInput)
    except Exception as e:
        return "Error. Cannot convert a String to Binary.\n"

    print("Input Number is:{}".format(n))
    answer = ""
    counter = 1
    keepgoing = True
    originalNumber = n

    if (n < 0):
        return "Error. Cannot convert a negative number to Binary.\n"
    if (n == 0 or n == 1):
        output = "Binary Equivalent of {} is {}\n".format(n,str(n))
        print(output)
        return output

    while (keepgoing):
        answer += str(n % 2)
        print("KeepGoing:{}; Counter:{}; N:{}; Answer:{}".format(keepgoing,counter,n,answer))
        
        n = n//2

        if (n == 1):
            keepgoing = False
            answer += "1"
            print("KeepGoing:{}; Counter:{}; N:{}; Answer:{}".format(keepgoing,counter,n,answer))
        
        counter = counter + 1
        
    output = "Binary Equivalent of {} is {}\n".format(originalNumber,answer[::-1])
    print(output)
    return output