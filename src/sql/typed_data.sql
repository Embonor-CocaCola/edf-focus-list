INSERT INTO public."FocusList"
    (
        "customerId",
        "suggestedEdf",
        "edfSubType",
        "edfSubtypeId",
        "createdAt",
        "updatedAt"
    )
    SELECT
        customer_id::INTEGER,
        suggested_edf,
        subtype_name,
        subtype_id::INTEGER,
        now() AS created_at,
        now() AS updated_at
    FROM
        temp_focus_list tmp
    INNER JOIN
    	"Customers" c ON tmp.customer_id ::numeric = c.id
    INNER JOIN
        "EquipmentSubtype" e ON tmp.subtype_id ::numeric = e.id;