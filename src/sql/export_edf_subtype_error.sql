COPY (
        SELECT
            customer_id::INTEGER,
            subtype_id::INTEGER,
            subtype_name,
            CONCAT('Edf Subtype ', subtype_id,' does not exist') AS error_message
        FROM
            temp_focus_list TMP
        LEFT JOIN
            "EdfSubtypes" C ON TMP.subtype_id ::numeric = C.id
        WHERE C.id IS NULL
    )
    TO STDOUT 
    WITH CSV HEADER;