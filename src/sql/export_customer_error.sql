COPY (
        SELECT
            customer_id::INTEGER,
            subtype_id::INTEGER,
            subtype_name,
            CONCAT('Customer ', customer_id,' does not exist') AS error_message
        FROM
            temp_focus_list TMP
        LEFT JOIN
            "Customers" C ON TMP.customer_id ::numeric = C.id
        WHERE C.id IS NULL
    )
    TO STDOUT 
    WITH CSV HEADER;