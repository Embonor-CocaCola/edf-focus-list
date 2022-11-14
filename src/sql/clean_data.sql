DELETE FROM
    public."FocusList"
WHERE
    "createdAt" < now() :: DATE - 365 :: INTEGER;