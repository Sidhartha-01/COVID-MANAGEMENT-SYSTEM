print("*******************************************************************************************") 

print("*                                                                                         *") 

print("*                    WELCOME TO COVID MANAGEMENT SYSTEM                                   *") 

print("*                                                                                         *") 

print("*******************************************************************************************") 

import mysql.connector 

mydb=mysql.connector.connect(host="localhost",user="root",password='*******') 

mycursor=mydb.cursor() 

mycursor.execute("create database if not exists covid_management") 

mycursor.execute("use covid_management") 

mycursor.execute("create table if not exists staff(sno varchar(25) not null, name varchar(25) not null, age varchar(25) not null, gender char(1) not null,post varchar(25) not null,salary varchar(25) not null)") 

mycursor.execute("create table if not exists patients(sno varchar(25) not null,name varchar(25) not null,age varchar(25) not null, gender varchar(25) not null, date date not null)") 

mycursor.execute("create table if not exists login(admin varchar(25) not null,password varchar(25) not null)") 

mycursor.execute("create table if not exists sno(patient varchar(25) not null,staff varchar(25) not null)") 

mycursor.execute("select * from sno") 

z=0 

for i in mycursor: 

    z=1 

if z==0: 

    mycursor.execute("insert into sno value('0','0')") 

mydb.commit() 

j=0 

mycursor.execute("select * from login") 

 

for i in mycursor: 

    j=1 

if j==0: 

    mycursor.execute("insert into login values('admin','admin')") 

    mydb.commit() 

loop1='y' 

while(loop1=='y' or loop1=='Y'): 

    print("________________________") 

    print("1.Admin") 

    print("2.Patient") 

    print("3.Exit") 

    print("________________________") 

    ch1=int(input("Enter your choice: ")) 

    if ch1==1: 

        pas=input("Enter your password: ") 

        mycursor.execute("select * from login") 

        for i in mycursor: 

            username,password=i 

        if pas==password: 

            loop2='n' 

            while(loop2=='n' or loop2=='N'): 

                print("_______________________") 

                print("1.Add patients") 

                print("2.Add staff") 

                print("3.Display Patients Record") 

                print("4.Display Staff Record") 

                print("5.Remove patients") 

                print("6.Remove Staff") 

                print("7.Logout") 

                print("_______________________") 

                ch2=int(input("Enter your choice: ")) 

                if ch2==1: 

                    loop3='y' 

                    while(loop3=='y' or loop3=='Y'): 

                        name=input("Enter patients name: ") 

                        age=input("Enter patients age: ") 

                        gender=input("Enter patients gender: ") 

                        date=input("Enter date of confirmation of covid: ") 

                        mycursor.execute("select * from sno") 

                        for i in mycursor: 

                            patient,staff=i 

                            patient=int(patient)+1 

 

                        mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"','"+date+"')") 

 

                        mycursor.execute("update sno set patient='"+str(patient)+"'") 

                        mydb.commit() 

                        print("data of Patient has been saved successfully..") 

                        mycursor.execute("select * from patients") 

                        t=0 

                        for i in mycursor: 

                            t+=1 

                            t_id1,name1,age1,gender1,date1=i 

                        print("Total number of Corona Infected patients-->", patient) 

 

                        print("Active Corona Cases-->", t) 

 

                        print("This patient with id", t_id1," will be in quarantine upto 14 days from",date1) 

 

                        loop3=input("Do you want to enter data of more Patients(y/n): ") 

                    loop2=input("Do you want to logout(y/n): ") 

                elif(ch2==2): 

                    loop3='y' 

                    while(loop3=='y' or loop3=='Y'): 

                        name=input("Enter new Staff name: ") 

                        age=input("Enter age: ") 

                        gender=input("Enter gender(m/f): ") 

                        post=input("Enter his/her post: ") 

                        salary=input("Enter his/her salary: ") 

 

                        mycursor.execute("select * from sno") 

                        for i in mycursor: 

                            patient,staff=i 

                            staff=int(staff)+1 

 

                        mycursor.execute("insert into staff values('"+str(staff)+"','"+name+"','"+age+"','"+gender+"','"+post+"','"+salary+"')") 

                        mycursor.execute("update sno set staff='"+str(staff)+"'") 

                        mydb.commit() 

                        print("staff with id",staff,"has been saved successfully...") 

 

                        mycursor.execute("select * from staff") 

                        t=0 

                        for i in mycursor: 

                            t+=1 

 

                        print("Active staff members-->",t) 

 

                        loop3=input("Do you want to enter more staff data(y/n) :") 

                    loop2=input("Do you want to logout(y/n): ") 

                elif ch2==3: 

                    idd=input("Enter patient's ID: ") 

                    t_id2,name2,age2,gender2,date2=["","","","",""] 

                    mycursor.execute("select * from patients where sno='"+idd+"'") 

                    for i in mycursor: 

                        t_id2,name2,age2,gender2,date2=i 

                    print("| ID | NAME | AGE | GENDER | CORONA POSITIVE DATE |") 

                    print("|",t_id2,"|",name2,"|",age2,"|",gender2,"|",date2,"|") 

                elif ch2==4: 

                    idd=input("Enter staff ID: ") 

                    t_id3,name3,age3,gender3,post3,salary3=["","","","","",""] 

                    mydb.commit() 

                    mycursor.execute("select * from staff where sno='"+idd+"'") 

                    for i in mycursor: 

                        t_id3,name3,age3,gender3,post3,salary3=i 

                    print("| ID | NAME | AGE | GENDER | POST | SALARY |") 

                    print("|",t_id3,"|",name3,"|",age3,"|",gender3,"|",post3,"|",salary3,"|") 

                elif ch2==5: 

                    loop3='y' 

                    while(loop3=='y' or loop3=='Y'): 

                        idd=input("Enter patient ID") 

                        mycursor.execute("delete from patients where sno='"+idd+"'") 

                        mydb.commit() 

                        print("Patient has been removed sucessfully") 

                        loop3=input("Do you want to remove more patients(y/n): ") 

 

                elif ch2==6: 

                    loop3='y' 

                    while(loop3=='y' or loop3=='Y'): 

                        idd=input("Enter staff ID") 

                        mycursor.execute("delete from staff where sno='"+idd+"'") 

                        mydb.commit() 

                        print("Staff has been removed successfully") 

                        loop3=input("Do you want to remove more staff(y/n): ") 

                elif ch2==7: 

                    break 

    elif ch1==2: 

        print("Thank you for coming forward for your test...") 

        icough=input("Are you feeling cough?(y/n): ").lower() 

        dry_cough='n' 

        cough='n' 

        if(icough=='y'): 

            dry_cough=input("Are you feeling dry cough(y/n): ").lower() 

            cough=input("Are you feeling normal cough(y/n): ").lower() 

 

        sneeze=input("Are you feeling sneeze?(y/n): ").lower() 

        pain=input("Are you feeling pain in your body?(y/n): ").lower() 

        weakness=input("Are you feeling weakness?(y/n): ").lower() 

        mucus=input("Are you feeling any mucus?(y/n): ").lower() 

        itemp=int(input("Please enter your temperature; ")) 

        if itemp<=100: 

            temp='low' 

        else: 

            temp='high' 

        breath=input("Are you having difficulty in breathing(y/n): ").lower() 

        if(dry_cough=='y' and sneeze=='y' and pain=='y' and weakness=='y' and temp=='high' and breath=='y'): 

            print("Sorry to say but according to us you are suffering from Corona......") 

            name=input("Enter your name: ") 

            age=input("Enter your age: ") 

            gender=input("Enter your gender(m/f): ") 

 

            mycursor.execute("select * from sno") 

            for i in mycursor: 

                patient,staff=i 

                patient=int(patient)+1 

            mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"',now())") 

            mycursor.execute("update sno set patient='"+str(patient)+"'") 

            mydb.commit() 

            print("data of patient has been saved successfully...") 

            print("Total number of Corona Infected patients-->",patient) 

            mycursor.execute("select * from patients") 

            t=0 

            for i in mycursor: 

                t+=1 

 

            print("Active corona cases-->",t) 

            mycursor.execute("select * from patients") 

            for i in mycursor: 

                t_id5,name5,age5,gender5,date5=i 

            print("This patient with id",t_id5,"will be in quarantine upto 14 days from",date5) 

        elif(dry_cough=='y' and sneeze=='y' and pain=='n' and weakness=='n' and temp=='low' and breath=='n'): 

            print("Nothing to worry, its just due to Air Pollution...") 

 

        elif(cough=='y' and mucus=='y' and sneeze=='y' and pain=='n' and weakness=='n' and temp=='low' and breath=='n'): 

            print("Nothing to worry, its just common cold...") 

        else: 

            print("You are not Corona Infected, it you are feeling something wrong, you just need to rest... ") 

            print("If then also you can't feel better, please consult to your doctor.") 

    elif ch1==3: 

        break 

print("THANK YOU") 

                 
