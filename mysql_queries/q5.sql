SELECT SUM(c) as c
FROM (
	SELECT COUNT(*) as c
	FROM pcap_data.packets
	WHERE handshake <> ""
) aux