#Author: AIM
#L3Cube Assignment No: 3
#Problem Statement: Display data present in the .pcap files

#This program analyses the data in the 'arp-storm.pcap'
#using the python-dpkt module. It prints the packet data and at the 
#end analyses the data based on total number of packet, number of ARP
#requests and replies.



import dpkt,socket
f=open("arp-storm.pcap","rb")
pcap = dpkt.pcap.Reader(f)
count=0
src_hardware=[]
target_hardware=[]
src_protocol=[]

operations=[]
req_count=0
rep_count=0

for ts,buf in pcap:
        count+=1
        print "\n\n\n"
        print "PACKET COUNT %d:\n"%count
        eth=dpkt.ethernet.Ethernet(buf)

        print "source=%s"%(eth.src).encode("hex")
	
        print "destination=%s"%(eth.dst).encode("hex")
	
        
	print "operation:%d"%eth.data.op
	operations.append(eth.data.op)
	if eth.data.op==1:
		req_count+=1
		print "ARP Request"
	else:
		rep_count+=1
		print "ARP Reply"
	
        print "source hardware address=%s"%(eth.data.sha).encode("hex")
	src_hardware.append((eth.data.sha).encode("hex"))

        print "target hardware address=%s"%(eth.data.tha).encode("hex")
	target_hardware.append((eth.data.tha).encode("hex"))	

        print "source protocol address=%s"%socket.inet_ntoa(eth.data.spa)
	src_protocol.append(socket.inet_ntoa(eth.data.spa))

        print "target protocol address=%s"%socket.inet_ntoa(eth.data.tpa)
	

f.close()
print "\nAnalysis\n"

src_hard = {x:src_hardware.count(x) for x in src_hardware}
print "Source Hardware Address : Number of times it occurs"
print src_hard

tar_hard = {x:target_hardware.count(x) for x in target_hardware}
print "Target Hardware Address : Number of times it occurs"
print tar_hard

src_pro = {x:src_protocol.count(x) for x in src_protocol}
print "Source Protocol Address : Number of times it occurs"
print src_pro

print "No of ARP requests: ",req_count
print "No of ARP replies:  ",rep_count

