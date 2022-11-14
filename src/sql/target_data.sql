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
        now(),
        now()
    FROM
        temp_focus_list TMP
    INNER JOIN
    	"Customers" C ON TMP.customer_id ::INTEGER = C.id
    INNER JOIN
        "EquipmentSubtype" E ON TMP.subtype_id ::INTEGER = E.id;