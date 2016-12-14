import pydivert

with pydivert.WinDivert("tcp and tcp.PayloadLength>0") as dev :
    for packet in dev :
        if(packet.is_outbound) :
            packet.tcp.payload = packet.tcp.payload.replace(b'Accept-Encoding: gzip, deflate, sdch',b'Accept-Encoding: gzip')
        if(packet.is_inbound) :
            packet.tcp.payload=packet.tcp.payload.replace(b'Michael',b'Gilvert')
        w.send(packet,recalculate_checksum=True)
        
