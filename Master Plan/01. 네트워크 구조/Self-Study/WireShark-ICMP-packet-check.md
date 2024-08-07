# 자율학습

수업시간에 네트워크 구조에 대해서 공부하면서   
WireShark 프로그램을 이용하여   
이더넷 Header를 확인하였다.

후에 WireShark 분석하는 데 도움이 되기 위해    
WireShark로 Ping Test를 보내서 패킷을 확인해보았다.

내 IP는 192.168.0.171 이다.   
![alt text](<ipconfig.png>)

그래서 다른 PC로 내 아이피로 핑을 보내보니까   
요청 시간이 만료되었습니다. 라고 되어있었다.
![alt text](<no response found.png>)

WireShark를 켜서 패킷을 확인해보니까 
![alt text](<WireShark no response.png>)
Source가 207에서   
Destination이 171으로   
ICMP 핑을 보내고 있는데 받아지지가 않는 것이다.

그래서 ICMP에 대해서 찾아보니까 
노트북에서 ICMP를 보안때문에 막고있을 수도 있다는 것이었다.

그래서 방화벽의 인바운드 규칙에서 ICMP를 찾아 
![alt text](<Inbound Rules.png>)

규칙을 허용해주었다.

그렇게 하고 다시 핑을 보내보았더니
![alt text](<Ping Test.png>)
핑이 잘 되는 것을 확인할 수 있었다.

그리고 WireShark 에서 다시 패킷을 확인해보았다.
![alt text](<WireShark ICMP.png>)
Frame, Ethernet, IPv4, ICMP 를 확인해볼 수 있었다.