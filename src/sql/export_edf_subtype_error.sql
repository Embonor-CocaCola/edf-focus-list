COPY (
        SELECT
            customer_id::INTEGER,
            subtype_id::INTEGER,
            subtype_name,
            CONCAT('Edf Subtype ', subtype_id,' does not exist') AS error_message
        FROM
            temp_focus_list tmp
        LEFT JOIN
            "EdfSubtypes" c ON tmp.subtype_id ::numeric = c.id
        WHERE c.id IS NULL
    )
    TO STDOUT 
    WITH CSV HEADER;