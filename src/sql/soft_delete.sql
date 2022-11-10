UPDATE public."FocusList"
SET "updatedAt" = now(), "deletedAt" = now()
    WHERE "deletedAt" IS NULL;