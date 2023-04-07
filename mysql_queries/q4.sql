SELECT src_ip, dst_ip
FROM (
	SELECT src_ip, dst_ip, SUM(length) as data_length
	FROM pcap_data.packets
	GROUP BY src_ip, dst_ip
	ORDER BY data_length DESC
) aux
LIMIT 1