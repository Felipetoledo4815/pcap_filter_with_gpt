SELECT SUM(c) as c
FROM (
	SELECT src_ip, dst_ip, COUNT(*) as c
	FROM pcap_data.packets
	WHERE (src_ip = "128.143.67.11" OR dst_ip = "128.143.67.11") AND handshake <> ""
	GROUP BY src_ip, dst_ip
) aux