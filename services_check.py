import os
import subprocess as sp
final_list=[]
insplit=[]
new_list=[]
#check status of all the installed services
all_services=sp.Popen(['service','--status-all'],stdout=sp.PIPE,stderr=sp.PIPE)
(out,err)=all_services.communicate()
services_list=out.decode()

#filters out the invalid_words from the given user query
invalid_words=['a','an','the','is','am','are','this','that','check','do','please','would','you','of','me','could','show','present','my','what','who','me','my','','tell','hey','all','in','under','then','will','would','for','there','command','find','my','run','execute','tell','year','server']
service_modes=['start','restart','status','stop','install']

#final list by replacing various factors
final_list=services_list.replace("[ - ]","").replace("[ + ]","").replace("  ","").replace(" ","")
user_input=input("Enter what do you want to do:")
user_input_list=user_input.split()

#removes out the invalid words
for my_val in user_input_list:
    if my_val not in invalid_words:
        insplit.append(my_val)
new_string=' '.join(insplit)

#checks the various modes of the service
for my_var in insplit:
    if my_var not in service_modes:
        new_list.append(my_var)
service_name=''.join(new_list)

#checks the services that whether or not it is apache2
if service_name=="apache":
    if "apache2" in final_list:
        #checks the various status
        if 'status' in insplit:
            command="systemctl status apache2.service"
            os.system(command)
        elif 'start' in insplit:
            command="systemctl start apache2.service"
            os.system(command)
        elif 'stop' in insplit:
            command="systemctl stop apache2.service"
            #print(command)
            os.system(command)
        elif "restart" in insplit:
            command="systemctl restart apache2.service"
            #print(command)
            os.system(command)
        elif "install" in insplit:
            command="sudo apt-get install apache2"
    else:
        #asks user if a service is not installed to install that service
        install=input("Do you want to install "+service_name)
        if install=='Yes' or install=="yes" or install=="y":
            installing_service="sudo apt-get install apache2"
            os.system(installing_service)
            print("==================")
            print("Service Installed")
else:
    print(insplit)
    #checks all the services
    if service_name in final_list:

        #checks the status of the given service
        if 'status' in insplit:
            command="systemctl status "+service_name
            os.system(command)

        #starts the given service
        elif 'start' in insplit:
            command="systemctl start "+service_name
            os.system(command)

        #stops the given service
        elif 'stop' in insplit:
            command="systemctl stop "+service_name
            #print(command)
            os.system(command)

        #restarts the given service
        elif "restart" in insplit:
            command="systemctl restart "+service_name
            #print(command)
            os.system(command)
        elif "install" in insplit:
            command="sudo apt-get install "+service_name
            os.system(command)
            print("Service Installed")
            #print(command)
    else:
        print("Service not installed")
        #print("Do you want to install that service")
        install=input("Do you want to install "+service_name)
        if install=='Yes' or install=="yes" or install=="y":
            installing_service="sudo apt-get install "+service_name
            os.system(command)
        else:
            print(" Thank you for using this program")
