SELECT protocol
FROM (
    SELECT protocol, COUNT(*) as c
	FROM pcap_data.packets
	GROUP BY protocol
	ORDER BY c DESC
) aux
LIMIT 1