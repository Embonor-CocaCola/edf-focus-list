COPY
    temp_focus_list
      (
        customer_id,
        suggested_edf,
        subtype_name,
        subtype_id
      )
  FROM
    STDIN
  WITH
    CSV HEADER
    DELIMITER ',';