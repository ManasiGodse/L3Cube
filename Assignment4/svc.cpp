//Author: AIM
//L3Cube Assignment No: 4
//Problem Statement: Create a simple version control (svc) program called "svc".
/*
This program is a simple version control program implemented using singly linked list.
The program creates a singly linked list which stores the version number and the data 
corresponding to that version. The program is in a menu driven format which provies 
four options: commit,see a specific version,see  the list of existing versions and exit.
Three functions commit(),display() and check_version() are defined. The commit() 
operation is called everytime any change is made to a file.

The particular change is saved and a new version corresponding to it is created.
This new version can be viewed by specifying the version number in option 2. Both append
and delete operations can be perfomed at a time and the length of each file is restricted 
to 20 lines. Every time a new version is created a new node is added to the linked list.
Then to check a particular version ,the version number specified is compared with every node's 
version number field and the matching data for the specified version is displayed.

NOTE: This program does not revert back to the version specified by svc N option. It only displays the content 
of the Nth version of the file.

Only one file is used i.e. test.txt
No other text file can be used
*/



#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int version_number=-1;
fstream myfile;
class node
{
	
public:
	string lines[20];
	int version;
	node *next;
	int no_of_lines;
	node()
	{
		for (int i=0;i<20;i++)
		{
			lines[i]='\0';
		}
		version=-1;
		next=NULL;
	}
	friend class svc_file;
};

class svc_file
{
	node *start;

public:
	svc_file()
	{
		start=NULL;
	}
	void commit();
	void display(int);
	void check_version();
};
//function to display the list of all the versions present.
void svc_file::check_version()
{
	node *temp=start;
	if(temp==NULL)
	{
		cout<<"No versions exists till now\n";
		return;
	}
	while(temp->next!=NULL)
	{
		cout<<"VERSION "<<temp->version<<endl;
		temp=temp->next;
	}
	cout<<"VERSION "<<temp->version<<endl;
}
//function to save the changes made to the file.
void svc_file::commit()
{
	int count=0;
	string l;
	if(version_number==-1) 
	{
		start=new node();	//create a start node if the linked list does not exist.
		myfile.open("test.txt");
		while(getline(myfile,l))
		{
			start->lines[count]=l;	//save the lines in the corresponding node.
			++count;
		}
		if (count>20)  //to check line limit
		{
			cout<<"Number of lines exceeded...cannot commit\n";
			delete start;
			return;
		}
		++version_number;
		start->no_of_lines=count;
		start->version=version_number;
		cout<<"File commit successfull\n";
		myfile.close();
	}
	else
	{
		node *save=new node(); //new node created for a new version. 
		myfile.open("test.txt");
		while(getline(myfile,l))
		{
			save->lines[count]=l;
			++count;
		}
		if (count>20) //to check the line limit.
		{
			cout<<"Number of lines exceeded...cannot commit\n";
			delete save;
			return;
		}
		++version_number;
		save->no_of_lines=count;
		save->version=version_number;
		node *temp=start;
		while(temp->next!=NULL)
		{
			temp=temp->next;
		}
		temp->next=save;
		save->next=NULL;
		
		myfile.close();
	}
}
//to display the data contained in a particular version.
void svc_file::display(int v)
{
	int flag=0;
	node *temp=start;
	
	if(temp==NULL)
	{
		cout<<"No commit made till now\n";
		return;
	}
	while(temp!=NULL)
	{
		if(temp->version==v)
		{
		flag=1;
		break;
		}	
		temp=temp->next;
	}
	if(flag==0)
	{
		cout<<"No such version exists\n";
		return;
	}
	cout<<"VERSION "<<temp->version<<endl;
	for(int i=0;i<temp->no_of_lines;i++)
	{
		cout<<temp->lines[i]<<endl;
	}
}
		
int main()
{

	svc_file f;
	string op1="svc";
	string op2="test.txt";
	string op_in1,op_in2;
	string o;
	int v,ch;
	do{
	cout<<"To commit press 1, to see a version press 2, to see how many versions exist press 3, to exit press 4\n";
	
	cin>>ch;
		switch(ch)
		{
			case 1:
			cout<<"USAGE: write svc test.txt to commit test.txt file\n";
			
			cin>>op_in1>>op_in2;
			if(op1.compare(op_in1)==0 && op2.compare(op_in2)==0)
			{
				f.commit();
			}
			break;

			case 2:
			cout<<"USAGE write svc N where N is the version_number you wish to see\n";
			cin>>o>>v;
			f.display(v);
			break;
	
			case 3:
			f.check_version();
			break;
	
			case 4: cout<<"Exiting from simple version control\n";
				return 0;
	
		}
	}while(ch!=4);
	return 0;
}







