import os
import getpass

password=getpass.getpass("Enter Password : ")
act_password='asks1012'
if password!=act_password:
	print('Incorrect authentication!')
	exit()

os.system('clear')
loc=input('Where do you want to run linux commands? local/remote : ')

if loc=='remote':
	usr=input('Enter remote username : ')
	ip=input('Enter the remote IP : ')
	os.system('tput setaf 3')
	print('Generating ssh key....')
	print('\n')
	print('NOTE : If you don\'t know about ssh-keygen, press Enter until you reach the step: "{}@{}\'s password"'.format(usr,ip))
	print('\n')
	print('Under "{}@{}\'s password", type the password of the username: "{}"'.format(usr,ip,usr))
	print('\n')
	os.system('tput setaf 7')
	os.system('ssh-keygen')
	os.system('ssh-copy-id {}@{}'.format(usr,ip))
	os.system('clear')
	os.system("tput setaf 6")


if loc=='local' or loc=='remote':
	while True:
		if loc=='local':
			os.system("tput setaf 6")
			print('''
				>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
														
				    88888888888   888     888   8888888    
					888       888     888     888      
					888       888     888     888      
					888       888     888     888      
					888        888888888    8888888    
														
				<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<''')
			os.system('tput setaf 3')
			print('''
			
				**** BASIC Linux Tasks ****

			Enter a1  : See Date and time
			Enter a2  : See Time continuously
			Enter a3  : See Calender
			Enter a4  : See the path of your current directory
			Enter a5  : Create a directory
			Enter a6  : Create a file
			Enter a7  : Detailed list of all files and directories inside some directory
			Enter a8  : Open or Edit a file in GUI or CLI
			Enter a9  : Speak out a word
			Enter a10 : See detailed information of all processes running
			Enter a11 : See the status of a system process
			Enter a12 : Start a system process
			Enter a13 : Stop a system process
			Enter a14 : Enable a system process
			Enter a15 : Disable a system process
			Enter a16 : Restart a system process
			Enter a17 : See all ports running on the system
			Enter a18 : Know the IP address
			Enter a19 : Remove a file
			Enter a20 : Remove a folder
			Enter a21 : Copy a file
			Enter a22 : Copy a folder
			Enter a23 : Move a file
			Enter a24 : Move a folder

				
				**** USER Related Tasks ****
			
			(Note : May require root previleges)
			Enter b1  : Add a user
			Enter b2  : Remove a user
			Enter b3  : Change password of a user
			Enter b4  : See the id of a user
			Enter b5  : See the details of logged in users

				
				**** SOFTWARE Installation Related Tasks ****
			
			(Note : May require root previleges)
			Enter c1  : Check if a software is installed (Ex: firefox,httpd...)
			Enter c2  : See all the installed software on your pc
			Enter c3  : See the path of a specific software which is already installed
			Enter c4  : Know the package name which provides a specific software
			Enter c5  : To install .rpm file
			Enter c6  : To uninstall a software
			Enter c7  : See all files associated in a package/software
			Enter c8  : Configure yum or add a repository
			Enter c9  : To install a software using yum(Configure yum first)
			Enter c10 : To configure a url using dnf

				
				**** COUNTING and SEARCHING mechanism ****

			Enter d1  : See number of lines in a file
			Enter d2  : See number of characters in a file
			Enter d3  : See the number of bytes of a file
			Enter d4  : See the number of words of a file
			Enter d5  : Show the lines starting with specific word or character in a file
			Enter d6  : Show the lines with specific order of characters in a file (Ex: 'od' in 'good','god')


				**** Storage and the Partitions ****

			Enter e1  : List all partitions in hard disk
			Enter e2  : Create a new partition
			Enter e3  : Delete a partition
			Enter e4  : Show the tree diagram of all partitions
			Enter e5  : Format a partition
			Enter e6  : Mount a partition
			Enter e7  : Unmount a partition
			Enter e8  : Show all mounted partitions
			Enter e9  : Edit the File System Table (fstab)


				**** Logical Volumes ****

			Enter f1 : Display all Physical Volumes
			Enter f2 : Display all Volume Groups
			Enter f3 : Display all Logical Volumes
			Enter f4 : Create a Physical Volume
			Enter f5 : Create a Volume Group
			Enter f6 : Create a Logical Volume


				**** Web ****

			Enter w  : Setup Web Server
			''')

			os.system('tput setaf 80')
			print('				Press e to exit!')

			os.system('tput setaf 7')
			print('Enter your choice: ',end='')
			choice=input()


			os.system('tput setaf 2')
			if choice=='a1' :
				os.system('date')
			elif choice=='a2' :
				os.system('while :; do echo -ne "   `date +%T``sleep 1`\b\b\b\b\b\b\b\b\b\b\b"; done &')
			elif choice=='a3' :
				print('Enter the name of month and press enter: ',end='')
				month=input()
				print('Enter the year: ',end='')
				year=input()
				os.system('cal {} {}'.format(month,year))
			elif choice=='a4':
				os.system('pwd')
			elif choice=='a5':
				print('Enter the name of directory and press enter: ',end='')
				directory=input()
				print('Enter the absolute path in which you want new directory, starting and ending with \"/\". For example \"/root/Desktop/\"  : ',end='')
				path1=input()
				os.system('mkdir {}{}'.format(path1,directory))
			elif choice=='a6':
				print('Enter the name of file and press enter: ',end='')
				filename=input()
				print('Enter the absolute path of the directory in which you want to save file, starting and ending with \"/\". For example \"/root/Desktop/\"  : ',end='')
				path2=input()
				os.system('touch {}{}'.format(path2,filename))
			elif choice=='a7':
				print("Enter the absolute path of the directory, starting and ending with \"/\". For example \"/root/Downloads/\" : ",end='')
				path3=input()
				os.system('ls -l {}'.format(path3))
			elif choice=='a8':
				print('Type \"gui\" or \"cli\" and press enter : ',end='')
				i=input()
				print('Enter the absolute path of the file, starting with \"/\". For example \"/root/Downloads/filename\" : ',end='')
				path4=input()
				print('\n')
				if i=='gui' or i=='GUI':
					os.system('gedit {}'.format(path4))
				elif i=='cli' or i=='CLI':
					os.system('vim {}'.format(path4))
			elif choice=='a9':
				print('Enter a word to speak out : ',end='')
				i1=input()
				os.system('espeak-ng {}'.format(i1))
			elif choice=='a10':
				os.system('ps -aux')
			elif choice=='a11':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('systemctl status {}'.format(process))
			elif choice=='a12':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('systemctl start {}'.format(process))
			elif choice=='a13':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('systemctl stop {}'.format(process))
			elif choice=='a14':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('systemctl enable {}'.format(process))
			elif choice=='a15':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('systemctl disable {}'.format(process))
			elif choice=='a16':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('systemctl restart {}'.format(process))
			elif choice=='a17':
				os.system('netstat -tnlp')
			elif choice=='a18':
				os.system('ifconfig')
			elif choice=='a19':
				filename=input('Enter the absolute path of file(Ex: /root/Desktop/filename) :\n')
				os.system('rm -f {}'.format(filename))
			elif choice=='a20':
				filename=input('Enter the absolute path of folder(Ex: /root/Desktop/foldername) :\n')
				os.system('rm -rf {}'.format(filename))
			elif choice=='a21':
				filename=input('Enter the absolute path of file(Ex: /root/Desktop/filename) :\n')
				destination=input('Enter the absolute path of the destination(Ex: /root/DestinationFolder) :\n')
				os.system('cp {} {}'.format(filename,destination))
			elif choice=='a22':
				filename=input('Enter the absolute path of folder(Ex: /root/Desktop/foldername) :\n')
				destination=input('Enter the absolute path of the destination(Ex: /root/DestinationFolder) :\n')
				os.system('cp -r {} {}'.format(filename,destination))
			elif choice=='a23':
				filename=input('Enter the absolute path of file(Ex: /root/Desktop/filename) :\n')
				destination=input('Enter the absolute path of the destination(Ex: /root/DestinationFolder) :\n')
				os.system('mv {} {}'.format(filename,destination))
			elif choice=='a24':
				filename=input('Enter the absolute path of folder(Ex: /root/Desktop/foldername) :\n')
				destination=input('Enter the absolute path of the destination(Ex: /root/DestinationFolder) :\n')
				os.system('mv {} {}'.format(filename,destination))
			elif choice=='b1':
				username1=input("Enter the username to be created : ")
				uid = int(input('Enter the User ID : '))
				cmd = input('Enter the Post Execution ')
				dir = input('Enter the Path of Home Directory for the user : ')
				x = os.system('sudo useradd -u {} -s {} -d {} {}'.format(uid,cmd,dir,username1))
				if x==0:
					os.system('passwd {}'.format(username1))
			elif choice=='b2':
				username2=input("Enter the username to be deleted : ")
				os.system('sudo userdel {}'.format(username2))
			elif choice=='b3':
				username3=input("Enter the username for which password is to be changed : ")
				os.system('sudo passwd {}'.format(username3))
			elif choice=='b4':
				username4=input("Enter the username : ")
				os.system('id {}'.format(username4))
			elif choice=='b5':
				os.system('w')
			elif choice=='c1':
				software=input('Enter the name of software (Ex : firefox) : ')
				os.system('sudo rpm -q {}'.format(software))
			elif choice=='c2':
				os.system('rpm -qa')
			elif choice=='c3':
				software=input('Enter the name of software (Ex : firefox) : ')
				os.system('which {}'.format(software))
			elif choice=='c4':
				software=input('Enter the name of software(Ex : firefox) : ')
				os.system('rpm -qf $(which {})'.format(software))
			elif choice=='c5':
				path=input('Enter the absolute path of .rpm file (Ex: /root/Downloads/file.rpm) : \n')
				os.system('sudo rpm -ivh {}'.format(path))
			elif choice=='c6':
				software=input('Enter the name of software (Ex : firefox) : ')
				os.system('sudo rpm -e {}'.format(software))
			elif choice=='c7':
				software=input('Enter the name of software (Ex : firefox) : ')
				os.system('rpm -ql {}'.format(software))
			elif choice=='c8':
				filename=input('Enter any name for your repo file without any extensions : ')
				os.system('touch /etc/yum.repos.d/{}.repo'.format(filename))
				package=input('Enter the path of the app package : \n')
				os.system('printf "[{}]\nbaseurl=file://{}\ngpgcheck=0\n" >>/etc/yum.repos.d/{}.repo'.format(filename,package,filename))
				os.system('yum repolist')
			elif choice=='c9':
				software=input('Enter the name of software(Ex: firefox) : ')
				os.system('yum install {}'.format(software))
			elif choice=='c10':
				link=input('Enter the url containing package : ')
				os.system('dnf install {}'.format(link))
			elif choice=='d1':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				os.system('wc -l {}'.format(path))
			elif choice=='d2':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				os.system('wc -m {}'.format(path))	
			elif choice=='d3':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				os.system('wc -c {}'.format(path))	
			elif choice=='d4':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				os.system('wc -w {}'.format(path))
			elif choice=='d5':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				search=input('Enter the word or character you want to search : ')
				os.system('grep --color=auto ^{} {}'.format(search,path))
			elif choice=='d6':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				search=input('Enter the word or character you want to search : ')
				os.system('tput setaf 7')
				os.system('grep --color=auto "{}" {}'.format(search,path))
				os.system('tput setaf 2')
			elif choice=='e1':
				os.system('fdisk -l')
			elif choice=='e2':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				os.system('tput setaf 17')
				print('''
	Note:
	Step1 : Enter 'n' for creating new partition
	Step2 : Enter 'p' for primary partition or 'e' for extending partition
	Step3 : Enter the start of first sector or choose default option
	Step4 : Enter the last sector or size of partition(Ex: +2G for 2GiB of partition)
	Step5 : Enter 'w' to save the partition
	Step6 : Enter 'q' to quit
				''')
				os.system('fdisk {}'.format(device))
			elif choice=='e3':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				os.system('tput setaf 17')
				print('''
	Note: 
	Step1 : Enter 'd' to delete a partition
	Step2 : Enter the number of partition(Ex: 1,2,3 or 4)
	Step3 : Enter 'w' to save
	Step4 : Enter 'q' to quit''')
				os.system('fdisk {}'.format(device))
			elif choice=='e4':
				os.system('lsblk')
			elif choice=='e5':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				frmat=input('Enter the type of format(Ex: ext4,ext3,...) : ')
				os.system('mkfs.{} {}'.format(frmat,device))
			elif choice=='e6':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				path=input('Enter the absolute path where to mount the device(Ex: /root/foldername) : \n')
				os.system('mount {} {}'.format(device,path))
			elif choice=='e7':
				path=input('Enter the absolute path where the device is mounted(Ex: /root/foldername) : \n')
				os.system('umount {}'.format(path))
			elif choice=='e8':
				os.system('df -h')
			elif choice=='e9':
				os.system('vim /etc/fstab')
			elif choice=='f1':
				os.system('pvdisplay')
			elif choice=='f2':
				os.system('vgdisplay')
			elif choice=='f3':
				os.system('lvdisplay')
			elif choice=='f4':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				os.system('pvcreate {}'.format(device))
			elif choice=='f5':
				n = int(input('Enter the number of devices you want to add to VG : '))
				l=[]
				for i in range(n):
					device = input('Enter Device{} : '.format(i+1))
					l.append(device)
				name = input('Enter a name for Volume Group : ')
				os.system('vgcreate {} {}'.format(name, ' '.join(l)))
			elif choice=='f6':
				size = input('Enter the size for Logical Volume in GiB (Ex: 2 for 2GiB) : ')
				name = input('Enter the name for Logical Volume : ')
				vg = input('Enter the Volume Group name : ')
				x = os.system('lvcreate --size {}G --name {} {}'.format(size, name, vg))
				if x==0:
					print('Formatting Logical Volume\n')
					os.system('mkfs.ext4 /dev/{}/{}'.format(vg, name))
					os.system('mkdir /{}'.format(name))
					x = os.system('mount /dev/{}/{} /{}'.format(vg, name, name))
					if x==0:
						print('Mounted Logical Volume at /{}'.format(name))
			elif choice=='w':
				print('Installing Httpd Software\n\n')
				os.system('yum install httpd -y')
				print('\nStarting & Enabling httpd Service\n\n')
				os.system('systemctl enable httpd --now')
				print('\nStopping firewall temporarily\n')
				os.system('systemctl stop firewalld')
			elif choice=='e':
				os.system('tput setaf 7')
				exit()
			else:
				print('Invalid choice!')


		elif loc=='remote':
			print('''
				>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
														
				    88888888888   888     888   8888888    
					888       888     888     888      
					888       888     888     888      
					888       888     888     888      
					888        888888888    8888888    
														
				<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<''')
			os.system('tput setaf 3')
			print('''
			
				**** BASIC Linux Tasks ****

			Enter a1  : See Date and time
			Enter a2  : See Calender
			Enter a3  : See the path of current directory of the remote user
			Enter a4  : Create a directory
			Enter a5  : Create a file
			Enter a6  : Detailed list of all files and directories inside some directory
			Enter a7  : Open or Edit a file in GUI or CLI
			Enter a8  : Speak out a word
			Enter a9  : See detailed information of all processes
			Enter a10 : See the status of a system process
			Enter a11 : Start a system process
			Enter a12 : Stop a system process
			Enter a13 : Enable a system process
			Enter a14 : Disable a system process
			Enter a15 : Restart a system process
			Enter a16 : See all ports running on the system
			Enter a17 : Know the IP address of remote server
			Enter a18 : Remove a file
			Enter a19 : Remove a folder
			Enter a20 : Copy a file
			Enter a21 : Copy a folder
			Enter a22 : Move a file
			Enter a23 : Move a folder

				
				**** USER Related Tasks ****
			
			(Note : May require root previleges)
			Enter b1  : Add a user
			Enter b2  : Remove a user
			Enter b3  : Change password of a user
			Enter b4  : See the id of a user
			Enter b5  : See the details of logged in users

				
				**** SOFTWARE Installation Related Tasks ****
			
			(Note : May require root previleges)
			Enter c1  : Check if a software is installed (Ex: firefox,httpd...)
			Enter c2  : See all the installed software on remote pc
			Enter c3  : See the path of a specific software which is already installed
			Enter c4  : Know the package name which provides a specific software
			Enter c5  : To install .rpm file
			Enter c6  : To uninstall a software
			Enter c7  : See all files associated in a package/software
			Enter c8  : Configure yum or add a repository
			Enter c9  : To install a software using yum(Configure yum first)
			Enter c10 : To configure a url using dnf

				
				**** COUNTING and SEARCHING mechanism ****

			Enter d1  : See number of lines in a file
			Enter d2  : See number of characters in a file
			Enter d3  : See the number of bytes of a file
			Enter d4  : See the number of words of a file
			Enter d5  : Search the lines starting with specific word or character in a file
			Emter d6  : show the lines with specific order of characters in a file (Ex: 'od' in 'good','god')


				**** SCP File Transfer ****

			Enter e1  : Upload a file to remote server
			Enter e2  : Download a file from remote server
			Enter e3  : Upload a folder to remote server
			Enter e4  : Download a folder from remote server
			
			
				**** Storage and the Partitions ****

			Enter f1  : List all partitions in hard disk
			Enter f2  : Create a new partition
			Enter f3  : Delete a partition
			Enter f4  : Show the tree diagram of all partitions
			Enter f5  : Format a partition
			Enter f6  : Mount a partition
			Enter f7  : Unmount a partition
			Enter f8  : Show all mounted partitions


				**** Logical Volumes ****

			Enter g1 : Display all Physical Volumes
			Enter g2 : Display all Volume Groups
			Enter g3 : Display all Logical Volumes
			Enter g4 : Create a Physical Volume
			Enter g5 : Create a Volume Group
			Enter g6 : Create a Logical Volume

				**** Web ****

			Enter w  : Setup Web Server
			''')

			os.system('tput setaf 80')
			print('				Press e to exit!')

			os.system('tput setaf 1')
			print('Enter your choice: ',end='')
			choice=input()


			os.system('tput setaf 2')
			if choice=='a1':
				os.system('ssh {} date'.format(ip))
			elif choice=='a2':
				print('Enter the name of month and press enter: ',end='')
				month=input()
				print('Enter the year: ',end='')
				year=input()
				os.system('ssh {} cal {} {}'.format(ip,month,year))
			elif choice=='a3':
				os.system('ssh {} pwd'.format(ip))
			elif choice=='a4':
				print('Enter the name of directory and press enter: ',end='')
				directory=input()
				print('Enter the absolute path in which you want new directory, starting and ending with \"/\". For example \"/root/Desktop/\"  : ',end='')
				path1=input()
				os.system('ssh {} mkdir {}{}'.format(ip,path1,directory))
			elif choice=='a5':
				print('Enter the name of file and press enter: ',end='')
				filename=input()
				print('Enter the absolute path of the directory in which you want to save file, starting and ending with \"/\". For example \"/root/Desktop/\"  : ',end='')
				path1=input()
				os.system('ssh {} touch {}{}'.format(ip,path1,filename))
			elif choice=='a6':
				print("Enter the absolute path of the directory, starting and ending with \"/\". For example \"/root/Downloads/\" : ",end='')
				path1=input()
				os.system('ssh {} ls -l {}'.format(ip,path1))
			elif choice=='a7':
				print('Type \"gui\" or \"cli\" and press enter : ',end='')
				i=input()
				print('Enter the absolute path of the file, starting with \"/\". For example \"/root/Downloads/filename\" : ',end='')
				path1=input()
				print('\n')
				if i=='gui' or i=='GUI':
					os.system('ssh {} gedit {}'.format(ip,path1))
				elif i=='cli' or i=='CLI':
					os.system('ssh {} vim {}'.format(ip,path1))
			elif choice=='a8':
				print('Enter a word to speak out : ',end='')
				i=input()
				os.system('ssh {} espeak-ng {}'.format(ip,i))
			elif choice=='a9':
				os.system('ssh {} ps -aux'.format(ip))
			elif choice=='a10':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('ssh {} systemctl status {}'.format(ip,process))
			elif choice=='a11':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('ssh {} systemctl start {}'.format(ip,process))
			elif choice=='a12':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('ssh {} systemctl stop {}'.format(ip,process))
			elif choice=='a13':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('ssh {} systemctl enable {}'.format(ip,process))
			elif choice=='a14':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('ssh {} systemctl disable {}'.format(ip,process))
			elif choice=='a15':
				process=input('Enter the name of the system process(Ex: firewalld) : ')
				os.system('ssh {} systemctl restart {}'.format(ip,process))
			elif choice=='a16':
				os.system('ssh {} netstat -tnlp'.format(ip))
			elif choice=='a17':
				os.system('ssh {} ifconfig'.format(ip))
			elif choice=='a18':
				filename=input('Enter the absolute path of file(Ex: /root/Desktop/filename) :\n')
				os.system('ssh {} rm -f {}'.format(ip,filename))
			elif choice=='a19':
				filename=input('Enter the absolute path of folder(Ex: /root/Desktop/foldername) :\n')
				os.system('ssh {} rm -rf {}'.format(ip,filename))
			elif choice=='a20':
				filename=input('Enter the absolute path of file(Ex: /root/Desktop/filename) :\n')
				destination=input('Enter the absolute path of the destination(Ex: /root/DestinationFolder) :\n')
				os.system('ssh {} cp {} {}'.format(ip,filename,destination))
			elif choice=='a21':
				filename=input('Enter the absolute path of folder(Ex: /root/Desktop/foldername) :\n')
				destination=input('Enter the absolute path of the destination(Ex: /root/DestinationFolder) :\n')
				os.system('ssh {} cp -r {} {}'.format(ip,filename,destination))
			elif choice=='a22':
				filename=input('Enter the absolute path of file(Ex: /root/Desktop/filename) :\n')
				destination=input('Enter the absolute path of the destination(Ex: /root/DestinationFolder) :\n')
				os.system('ssh {} mv {} {}'.format(ip,filename,destination))
			elif choice=='a23':
				filename=input('Enter the absolute path of folder(Ex: /root/Desktop/foldername) :\n')
				destination=input('Enter the absolute path of the destination(Ex: /root/DestinationFolder) :\n')
				os.system('ssh {} mv {} {}'.format(ip,filename,destination))
			elif choice=='b1':
				username=input("Enter the username to be created : ")
				os.system('ssh {} sudo useradd {}'.format(ip,username))
			elif choice=='b2':
				username=input("Enter the username to be deleted : ")
				os.system('ssh {} sudo userdel {}'.format(ip, username))
			elif choice=='b3':
				username=input("Enter the username for which password is to be changed : ")
				os.system('ssh {} sudo passwd {}'.format(ip,username))
			elif choice=='b4':
				username4=input("Enter the username : ")
				os.system('ssh {} id {}'.format(ip,username4))
			elif choice=='b5':
				os.system('w')
			elif choice=='c1':
				software=input('Enter the name of software (Ex : firefox) : ')
				os.system('ssh {} sudo rpm -q {}'.format(ip,software))
			elif choice=='c2':
				os.system('ssh {} rpm -qa'.format(ip))
			elif choice=='c3':
				software=input('Enter the name of software (Ex : firefox) : ')
				os.system('ssh {} which {}'.format(ip,software))
			elif choice=='c4':
				software=input('Enter the name of software(Ex : firefox) : ')
				os.system('ssh {} rpm -qf $(which {})'.format(ip,software))
			elif choice=='c5':
				path=input('Enter the absolute path of .rpm file (Ex: /root/Downloads/file.rpm) : \n')
				os.system('ssh {} sudo rpm -ivh {}'.format(ip,path))
			elif choice=='c6':
				software=input('Enter the name of software (Ex : firefox) : ')
				os.system('ssh {} sudo rpm -e {}'.format(ip,software))
			elif choice=='c7':
				software=input('Enter the name of software (Ex : firefox) : ')
				os.system('ssh {} rpm -ql {}'.format(ip,software))
			elif choice=='c8':
				filename=input('Enter any name for your repo file without any extensions : ')
				os.system('ssh {} "touch /etc/yum.repos.d/{}.repo"'.format(ip,filename))
				reponame=input('Enter any name for your repo : ')
				package=input('Enter the path of the app package : \n')
				os.system('ssh {} "printf \'\n[{}]\nbaseurl=file://{}\ngpgcheck=0\n\' >>/etc/yum.repos.d/{}.repo"'.format(ip,reponame,package,filename))
				os.system('ssh {} yum repolist'.format(ip))
			elif choice=='c9':
				software=input('Enter the name of software(Ex: firefox) : ')
				os.system('ssh {} yum install {}'.format(ip,software))
			elif choice=='c10':
				link=input('Enter the url containing package : ')
				os.system('ssh {} dnf install {}'.format(ip,link))
			elif choice=='d1':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				os.system('ssh {} wc -l {}'.format(ip,path))
			elif choice=='d2':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				os.system('ssh {} wc -m {}'.format(ip,path))
			elif choice=='d3':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				os.system('ssh {} wc -c {}'.format(ip,path))
			elif choice=='d4':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				os.system('ssh {} wc -w {}'.format(ip,path))
			elif choice=='d5':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				search=input('Enter the word or character you want to search : ')
				os.system('ssh {} grep --color=auto ^{} {}'.format(ip,search,path))
			elif choice=='d6':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				search=input('Enter the word or character you want to search : ')
				os.system('ssh {} grep --color=auto "{}" {}'.format(ip,search,path))
			elif choice=='e1':
				path=input('Enter the absolute path of the file (Ex: /root/Downloads/file) : \n')
				path2=input('Enter the absolute path of target location (Ex: /root/Downloads/) : \n')
				os.system('scp {} {}:{}'.format(path,ip,path2))	
			elif choice=='e2':
				path=input('Enter the absolute path of the file on server (Ex: /root/Downloads/file) : \n')
				path2=input('Enter the absolute path where to download file (Ex: /root/Downloads/) : \n')
				os.system('scp {}:{} {}'.format(ip,path,path2))	
			elif choice=='e3':
				path=input('Enter the absolute path of the folder (Ex: /root/folder/) : \n')
				path2=input('Enter the absolute path of target location (Ex: /root/Downloads/) : \n')
				os.system('scp -r {} {}:{}'.format(path,ip,path2))	
			elif choice=='e4':
				path=input('Enter the absolute path of the folder on server (Ex: /root/Downloads/folder/) : \n')
				path2=input('Enter the absolute path where to download folder (Ex: /root/Downloads/) : \n')
				os.system('scp -r {}:{} {}'.format(ip,path,path2))
			elif choice=='f1':
				os.system('ssh {} fdisk -l'.format(ip))
			elif choice=='f2':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				os.system('tput setaf 17')
				print('''
	Note:
	Step1 : Enter 'n' for creating new partition
	Step2 : Enter 'p' for primary partition or 'e' for extending partition
	Step3 : Enter the start of first sector or choose default option
	Step4 : Enter the last sector or size of partition(Ex: +2G for 2GiB of partition)
	Step5 : Enter 'w' to save the partition
	Step6 : Enter 'q' to quit
				''')
				os.system('ssh {} fdisk {}'.format(ip,device))
			elif choice=='f3':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				os.system('tput setaf 17')
				print('''
	Note: 
	Step1 : Enter 'd' to delete a partition
	Step2 : Enter the number of partition(Ex: 1,2,3 or 4)
	Step3 : Enter 'w' to save
	Step4 : Enter 'q' to quit
				''')
				os.system('ssh {} fdisk {}'.format(ip,device))
			elif choice=='f4':
				os.system('ssh {} lsblk'.format(ip))
			elif choice=='f5':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				frmat=input('Enter the type of format(Ex: ext4,ext3,...) : ')
				os.system('ssh {} mkfs.{} {}'.format(ip,frmat,device))
			elif choice=='f6':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				path=input('Enter the absolute path where to mount the device(Ex: /root/foldername) : \n')
				os.system('ssh {} mount {} {}'.format(ip,device,path))
			elif choice=='f7':
				path=input('Enter the absolute path where the device is mounted(Ex: /root/foldername) : \n')
				os.system('ssh {} umount {}'.format(ip,path))
			elif choice=='f8':
				os.system('ssh {} df -h'.format(ip))	
			elif choice=='g1':
				os.system('ssh {} pvdisplay'.format(ip))
			elif choice=='g2':
				os.system('ssh {} vgdisplay'.format(ip))
			elif choice=='g3':
				os.system('ssh {} lvdisplay'.format(ip))
			elif choice=='g4':
				device=input('Enter the name of the device(Ex: /dev/sda) : ')
				os.system('ssh {} pvcreate {}'.format(ip,device))
			elif choice=='g5':
				n = int(input('Enter the number of devices you want to add to VG : '))
				l=[]
				for i in range(n):
					device = input('Enter Device{} : '.format(i+1))
					l.append(device)
				name = input('Enter a name for Volume Group : ')
				os.system('ssh {} vgcreate {} {}'.format(ip, name, ' '.join(l)))
			elif choice=='g6':
				size = input('Enter the size for Logical Volume in GiB (Ex: 2 for 2GiB) : ')
				name = input('Enter the name for Logical Volume : ')
				vg = input('Enter the Volume Group name : ')
				x = os.system('ssh {} lvcreate --size {}G --name {} {}'.format(ip, size, name, vg))
				if x==0:
					print('Formatting Logical Volume\n')
					os.system('ssh {} mkfs.ext4 /dev/{}/{}'.format(ip, vg, name))
					os.system('ssh {} mkdir /{}'.format(ip, name))
					x = os.system('ssh {} mount /dev/{}/{} /{}'.format(ip, vg, name, name))
					if x==0:
						print('Mounted Logical Volume at /{}'.format(name))
			elif choice=='w':
				print('Installing Httpd Software\n\n')
				os.system('ssh {} yum install httpd -y'.format(ip))
				print('\nStarting & Enabling httpd Service\n\n')
				os.system('ssh {} systemctl enable httpd --now'.format(ip))
				print('\nStopping firewall temporarily\n')
				os.system('ssh {} systemctl stop firewalld'.format(ip))
			elif choice=='e':
				os.system('tput setaf 7')
				exit()
			else:
				print('Invalid choice!')
			
		os.system("tput setaf 7")
		input('Press Enter to continue....')
		os.system('clear')

else:
	print('invalid choice!')