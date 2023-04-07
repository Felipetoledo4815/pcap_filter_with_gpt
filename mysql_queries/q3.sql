SELECT src_ip, dst_ip
FROM (
	SELECT src_ip, dst_ip, COUNT(*) as C
	FROM pcap_data.packets
	WHERE protocol = "TCP"
	GROUP BY src_ip, dst_ip
	ORDER BY c DESC
) aux
LIMIT 1