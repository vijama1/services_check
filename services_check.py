import os
import subprocess as sp
final_list=[]
insplit=[]
new_list=[]
all_services=sp.Popen(['service','--status-all'],stdout=sp.PIPE,stderr=sp.PIPE)
(out,err)=all_services.communicate()
services_list=out.decode()
invalid_words=['a','an','the','is','am','are','this','that','check','do','please','would','you','of','me','could','show','present','my','what','who','me','my','','tell','hey','all','in','under','then','will','would','for','there','command','find','my','run','execute','tell','year','server']
service_modes=['start','restart','status','stop']
final_list=services_list.replace("[ - ]","").replace("[ + ]","").replace("  ","").replace(" ","")
#final_list=services_list.replace("[","").replace("+","").replace("-"," ").replace("]","").replace("  ","").replace(" ","")
#final_list=services_list[]
user_input=input("Enter what do you want to do:")
#print(final_list)
if final_list.find('rpcbiaand')>=0:
    print("FOund")
user_input_list=user_input.split()
#print(user_input_list)
for my_val in user_input_list:
    if my_val not in invalid_words:
        insplit.append(my_val)
new_string=' '.join(insplit)
#print(insplit)
for my_var in insplit:
    if my_var not in service_modes:
        new_list.append(my_var)
service_name=''.join(new_list)
#print(service_name)
#print(service_name)
if service_name=="apache":
    if "apache2" in final_list:
        if 'status' in insplit:
            command="systemctl status "+service_name
            os.system(command)
        elif 'start' in insplit:
            command="systemctl start "+service_name
            os.system(command)
        elif 'stop' in insplit:
            command="systemctl stop "+service_name
            #print(command)
            os.system(command)
        elif "restart" in insplit:
            command="systemctl restart "+service_name
            #print(command)
            os.system(command)
    else:
        install=input("Do you want to install "+service_name)
        if install=='Yes' or install=="yes" or install=="y":
            installing_service="sudo apt-get install apache2"
            print(installing_service)
if service_name!="apache":
    if service_name in final_list:
        if 'status' in insplit:
            command="systemctl status "+service_name
            os.system(command)
        elif 'start' in insplit:
            command="systemctl start "+service_name
            os.system(command)
        elif 'stop' in insplit:
            command="systemctl stop "+service_name
            #print(command)
            os.system(command)
        elif "restart" in insplit:
            command="systemctl restart "+service_name
            #print(command)
            os.system(command)
    else:
        print("Service not installed")
        #print("Do you want to install that service")
        install=input("Do you want to install "+service_name)
        if install=='Yes' or install=="yes" or install=="y":
            installing_service="sudo apt-get install "+service_name
            print(installing_service)
        else:
            print(" Thank you for using this program")
        #os.system()
#print(new_list)
