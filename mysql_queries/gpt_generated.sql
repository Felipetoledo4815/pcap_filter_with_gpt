-- SELECT src_ip
-- FROM packets
-- WHERE protocol = 'TCP'
-- GROUP BY src_ip
-- ORDER BY COUNT(*) DESC
-- LIMIT 1;

-- SELECT src_ip
-- FROM packets
-- GROUP BY src_ip
-- ORDER BY SUM(length) DESC
-- LIMIT 1;

-- SELECT src_ip, dst_ip
-- FROM packets
-- WHERE protocol = 'TCP'
-- GROUP BY src_ip, dst_ip
-- ORDER BY COUNT(*) DESC
-- LIMIT 10;

-- SELECT src_ip, dst_ip
-- FROM packets
-- GROUP BY src_ip, dst_ip
-- ORDER BY SUM(length) DESC
-- LIMIT 10;

-- SELECT COUNT(*) as handshake_count
-- FROM packets
-- WHERE src_ip = '128.143.67.11' AND handshake != '';

-- SELECT COUNT(*) as handshake_count
-- FROM packets
-- WHERE handshake != '';

-- SELECT protocol, COUNT(*) as protocol_count
-- FROM packets
-- GROUP BY protocol
-- ORDER BY protocol_count DESC
-- LIMIT 1;
