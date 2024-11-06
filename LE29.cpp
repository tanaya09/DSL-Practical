#include<bits/stdc++.h>
using namespace std;

#define MAX 5

class Queue
{
	private : 
	int f=0;
	int r=0;
	struct info
	{
		int id;
		string description;
	};
	info arr[MAX];
	
	public: 
	void insert();
	void display();
	void del();
	bool size();
};

int main()
{
	int choice=1;
	Queue q;
	do{
		cout<<"\n--------------- MENU ------------- \n";
		cout<<"1. Insert jobs \n";
		cout<<"2. Delete jobs \n";
		cout<<"3. Display jobs \n";
		cout<<"0. Exit\n";
		cout<<"\nEnter choice : ";
		cin>>choice;
		switch(choice)
		{
			case 1 : q.insert();
					break;
			case 2 : q.del();
					break;
			case 3 : q.display();
					break;
			case 0 : break;
			default : cout<<"\nEnter correct choice \n";
		}
	}while(choice!=0);
	cout<<"\nOut of the program\n";
	

	cout<<"\n";
	system("pause");
	return 0;
}

void Queue::display()
{
	cout<<"\nPrinting the queue : \n";
	for(int i=f;i<r;i++)
	{
		cout<<"\nJob number : "<<arr[i].id;
		cout<<"\nJob description : "<<arr[i].description;
		cout<<"\n";
	}	
}

void Queue::del()
{
	if(!size())
	{
		arr[f].id = 0;
		arr[f].description = "";
		f++;
	}
	else
	{
		cout<<"\nQueue is empty\n";
	}
}

bool Queue::size()
{
	int size = r-f;
	return 0==size;
}

void Queue::insert()
{
	
	int i=r;
	char choice='y';
	if(r<MAX)
	{
		do{
			cout<<"\nEnter job id : ";
			cin>>arr[i].id;
			cout<<"\nEnter job description : ";
			cin.get();
			getline(cin,arr[i].description);
			if(i==0)
			{
				f=i;
			}
			cout<<"\nDo you want to enter more jobs? (y/n) : ";
			cin>>choice;
			r++;
			i++;
		}while(choice=='y' && i<MAX);
	}
	else
	{
		cout<<"\nCan't add more jobs, the queue is full\n";
	}
}