"""
select and format date

"""

query = "
SELECT gfct_dtfct AS invoice_date,
       gfct_num   AS invoice_id,
       case
           when length(trim(gfct_dtech)) = 5 then to_char(to_date(trim(gfct_dtech), 'MM/YY'), 'yyyyMMddHHmmss')
           when length(trim(gfct_dtech)) = 6 AND trim(gfct_dtech) NOT LIKE '0000%'
               then to_char(to_date(trim(gfct_dtech), 'YYYYMM'), 'yyyyMMddHHmmss')
           when length(trim(gfct_dtech)) = 7 then to_char(to_date(trim(gfct_dtech), 'MM/YYYY'), 'yyyyMMddHHmmss')
           when length(trim(gfct_dtech)) = 8 then to_char(to_date(trim(gfct_dtech), 'YYYYMMDD'), 'yyyyMMddHHmmss')
           when length(trim(gfct_dtech)) = 10 AND trim(gfct_dtech) LIKE '%-%'
               then to_char(to_date(trim(gfct_dtech), 'YYYY-MM-DD'), 'yyyyMMddHHmmss')
           when length(trim(gfct_dtech)) = 10 AND trim(gfct_dtech) LIKE '%/%'
               then to_char(to_date(trim(gfct_dtech), 'DD/MM/YYYY'), 'yyyyMMddHHmmss')
           when length(trim(gfct_dtech)) = 21 then to_char(to_date(split_part(trim(gfct_dtech), '-', 2), 'DD/MM/YYYY'),
                                                           'yyyyMMddHHmmss')
           end    AS due_date,
       gfct_mnt   as invoice_amount
FROM getifactures"
