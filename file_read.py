

"""
 * @author [Srijan Kumar]
 * @email [www.srijankumar@gmail.com]
 * @create date 2021-07-24 10:42:53
 * @modify date 2021-07-27 10:48:03
 * @desc [Mat design]
""" 

 



import time


def mat_print(row,col,spchar):
   """This is mat design with python.\n Enjoy! \n (!run program for instructions :D)"""
   for i in range(row):
        if i==0:
            # print("-"*row)
            if spchar==" ":
                print("|",end="")
                print("-"*col,end="|")
                print()
            else:
                print("|",end="")
                print(spchar*col,end="|")
                print()

          
        elif i>0 and i!=row-1:
                        # print(l.centre(row,'-'))
            print("|",end="")
            print(spchar*col,end="|")
            print()

        else:
            if i==row-1:
                if spchar==" ":
                    print("|",end="")
                    print("-"*col,end="|")
                    print()
                else:
                    print("|",end="")
                    print(spchar*col,end="|")
                    print()

# Main program

if __name__ == "__main__":
    
    cond=True    

    while cond==True:

        str1="""This Function give you designed mates with the help of python!\n1.Enter number of rows and column (if row and column are same type \"0\" before value.!)\n2.Enter characterof mat (press <space> for blank design)\n3.Approve design or create more!\n4.Press \"q\" for exit on any step.  """

        print(str1)

        print()

        l1=[] #This is List.

        #Rows
        raw=input("Enter no. of rows:\n (note!:if row and column are same type \"0\" before value.)  \n--> ")

        if raw=="q":
            print("Closing Program..")
            time.sleep(2.5)
            break

        for i in (raw):
            l1.append(i)
  
        r=int(raw)

        print()

        #Columns
        if l1[0]=='0':
            c=r
        else:
            raw_col=input("Enter no. of column:\n --> ")
            if raw_col=="q":
                print("Closing Program..")
                time.sleep(2.5)
                break
            elif raw_col.isnumeric()==True:
                c=int(raw_col)
            else:
                print("Enter Either \'q\' or a number")
                time.sleep(2.5)
                break


        #Special Character taken
        spc=input("Enter Design(press <space> for blank design):\n --> ")
        if spc=="q":
            time.sleep(2.5)
            break

        if spc==" ":
            print("<space> key hit!")
            print()
        mat_print(r,c,spc)
        print()

        app=input("approed?(y/n) :")

        if app=="y":
            print("We are glad!")
            time.sleep(2.5)
            cond=False
        elif app=="n":
            cond=True
        elif app=="q":
            time.sleep(2.5)
            break
            


