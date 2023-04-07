SELECT src_ip
FROM (
	SELECT src_ip, COUNT(src_ip) as pkg_sent
	FROM pcap_data.packets
	WHERE protocol = "TCP"
	GROUP BY src_ip
	ORDER BY pkg_sent DESC
) aux
LIMIT 1