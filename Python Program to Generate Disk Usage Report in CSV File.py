#Required Modules
#We will be using 4 methods here, the modules required would be Shutil, pandas, WMI, OS, and subprocess.

#WMI – WMI is a set of specifications from Microsoft for consolidating the management of devices and applications in a network from Windows computing systems. WMI provides users with data regarding the condition of native or remote pc systems. 
#We will use shutil and WMI in different methods, but pandas will be common in both of them, so to install pandas, write the following command in the VScode terminal/ Pycharm terminal or normal Command Prompt.
#pip install pandas

#Using WMI Module to Generate Disk Usage Report in CSV File
#Using the WMI module we can easily fetch the name of the disk, the total size of that disk, and the amount of free space it has (both in bytes). Install the WMI module using the following command:

#pip install WMI
#Here take a variable called key(user can use any name) to initialize the WMI method of the WMI module using which we will get the usage report, then next 3 lines are just 3 blank lists to store the drive name, free_space and total_size of that drive.



import wmi
import pandas as pd

key=wmi.WMI()
drive_name=[]
free_space=[]
total_size=[]

for drive in key.win32_LogicalDisk():
    drive_name.append(drive.Caption)
    free_space.append(round(int(drive.FreeSpace)/1e+9,2))
    total_size.append(round(int(drive.Size)/1e+9,2))
    print("================")
    print("Drive Name: ", drive.Caption+"\n====================",
    "\nFree Space Available in GB: \n", round(
    int(drive.FreeSpace)/1e+9,2),
    "\nTotal Size in GB :\n", round(int(drive.Size)/1e+9,2))

size_dict={'Dictionary Name:': drive_name,
           'Free Space (in GB)': free_space,
           'Total Size (in GB)' :total_size}

data_frame=pd.DataFrame(size_dict)
data_frame.to_csv("disk_usage.csv")

