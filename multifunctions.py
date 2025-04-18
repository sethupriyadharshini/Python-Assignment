class multipleFunctions:
    def Subfields():
        lists = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in lists:
            print(temp)

    def oddEven():
        num = int(input("Enter a number:"))
        if(num%2==0):
            print(num, "is Even number")
        else:
            print(num, "is Odd number")

    def Elegible():
        gender="Male"
        age=20
        if(gender == "Male" and age>=21):
            print("Your Gender:"+gender, "\nYour Age:"+str(age))
            print("ELIGIBLE")
        elif(gender == "Female" and age>=18):
            print("Your Gender:"+gender, "\nYour Age:"+str(age))
            print("ELIGIBLE")
        else:
            print("Your Gender:"+gender, "\nYour Age:"+str(age))
            print("NOT ELIGIBLE")

    def percentage():
        Subject1=98
        Subject2=87
        Subject3=95
        Subject4=95
        Subject5=93
        total = Subject1+Subject2+Subject3+Subject4+Subject5
        percentage = total/5
        print("Subject1= "+str(Subject1)+"\nSubject2= "+str(Subject2)+"\nSubject3= "+str(Subject3)+"\nSubject4= "+str(Subject4)+"\nSubject5= "+str(Subject5))
        print("Total : ",total)        
        print("Percentage : ", percentage)

    def triangle():
        Height=32
        Breadth=34
        areaOfTriangle=(Height*Breadth)/2
        print("Height: "+str(Height)+"\nBreadth: "+str(Breadth))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", areaOfTriangle)
        Height1=2
        Height2=4
        Breadth1=4
        perimeterOfTriangle=Height1+Height2+Breadth1
        print("Height1: "+str(Height1)+"\nHeight2: "+str(Height2)+"\nBreadth1: "+str(Breadth1))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ", perimeterOfTriangle)