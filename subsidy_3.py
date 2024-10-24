
print ("CALCULATION OF SUBSIDY FOR ENERGY COST")

m =int(input("Enter the number of the months you wish to apply for subsidy(one up to four )\n"))

l=[]
print("------------------------------------------------")
     
for i in range(1,m+1) :
	 k=int(input("Enter your consumption for every month\n"))
	 l.append(k)
	
print("------------------------------------------------")
print("Print the length of our list")
k=len(l)
print("The length of our list is %d\n"%(k))

print("------------------------------------------------")
print ("Monthly  Consumption") 
for i in range(0,k):
	 print("%d       %d"% (i,l[i]))

print("------------------------------------------------")
f=0.2
s=0.1
subsidy=0.0
total=0.0
for i in range(0,k):
	if  l[i]<=500:
		     subsidy=l[i]*f
		     print("The sibsidy for the %dst month is %.2f"%(i+1, subsidy))
		     
	elif l[i]>=501:
    		   subsidy=l[i]*s
    		   print("The sibsidy for the %dst month is %.2f"%(i+1, subsidy))
    		   total=total+subsidy
      


	
    
    		  
    		    
   		    
   		     
    		   
		        



