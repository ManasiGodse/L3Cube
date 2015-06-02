#Author: AIM
#L3Cube Assignment No: 3
#Problem Statement: Display data present in the .pcap files

#This program analyses the data in the 'tcp-ecn-sample.pcap'
#using the python-dpkt module. It prints the packet data and at the 
#end analyses the data based on total number of packet, number of HTTP
#requests and responses





import dpkt,socket
f=open('tcp-ecn-sample.pcap','rb')
pcap = dpkt.pcap.Reader(f)
count=0
count_req=0
count_res=0

for ts,buf in pcap:
        eth=dpkt.ethernet.Ethernet(buf)
        print (eth.dst).encode("hex")   
        print (eth.src).encode("hex")   
        ip_temp=eth.data
        if ip_temp.p==dpkt.ip.IP_PROTO_TCP:
            count=count+1
            print "\n\nIP PACKET NUMBER %d"%count
            print "tos:%d"%ip_temp.tos
            print "source address:%s"%socket.inet_ntoa(ip_temp.src)
            print "destination address:%s"%socket.inet_ntoa(ip_temp.dst)
            encap_tcp=ip_temp.data
            print "source port:%d"%encap_tcp.sport
            print "destination port:%d"%encap_tcp.dport
	    if encap_tcp.dport==80:
		print "Packet for HTTP Request"
		count_req+=1
	    if encap_tcp.sport==80:
		print "Packet for HTTP Response"
		count_res+=1
            print "urgent pointer:%d"%encap_tcp.urp
            print "seq :%d"%encap_tcp.seq
            print "ack:%d"%encap_tcp.ack
    

print "\n\nAnalysis\n\n"     
print "Total IP packets: ",count
print "Total HTTP Requests: ",count_req
print "Total HTTP Responses: ",count_res        
