ACL 접근 통제 실습을 하기 위해서

Cisco Packet Tracer에서 

1. R1에 외부망 20.20.20.0/24 에서 내부망 192.168.10.10/24 로 ping 접근하는 것으로 차단
2. R1에 내부망 192.168.10.0/24 에서 외부망 20.20.20.0/24 로 ping 접근하는 모든 서비스 차단

20.20.20.0/24 로 문제에서 나오기 때문에   
ACL 명령어를 조금 수정해주었다

```
access-list 111 deny tcp 20.20.20.0 0.0.0.255 host 192.168.10.10 eq 80
access-list 111 permit ip any any
interface fa0/0
ip access-group 111 in
```

차단이 되지 않고    
20.20.20.20 PC에서 192.168.10.10 PC로 핑이 잘 나가는 것을 확인

```
access-list 112 deny tcp host 20.20.20.20 host 192.168.10.10 eq 80
access-list 112 permit ip any any
interface fa0/0
ip access-group 112 in
```
이것 또한 차단 안되었음.

```
access-list 113 deny ip host 20.20.20.20 host 192.168.10.10
access-list 113 permit ip any any
interface fa0/0
ip access-group 113 in
```
이것도 차단이 안되었음

```
access-list 111 deny icmp 20.20.20.0 0.0.0.255 host 192.168.10.10 echo
access-list 111 deny ip 20.20.20.0 0.0.0.255 host 192.168.10.10 
access-list 111 permit ip any any
```
이것도 안됨

이유가 뭔지모르겠음... 질문