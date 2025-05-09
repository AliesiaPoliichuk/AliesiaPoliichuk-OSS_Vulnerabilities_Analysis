create table pa_cve_data_new (
  cve_id varchar(50) primary key,
  cwe_id varchar(50) not null,
  description text,
  status varchar(50),
  created_at timestamp,
  modified_at timestamp,
  vendor varchar(100),
  product varchar(100)
  )
  
  
  select *
  from pa_cve_data_new 
  
  select count (*)
  from pa_cve_data_new
  
  -- графік 1
select 
	extract( year from created_at) as year,
	count (*) as vulnerabilities_count
from pa_cve_data_new pcd 
group by 1
order by 1
;


-- графік 2 
select
    product,
    count(*) as vulnerabilities_count
from pa_cve_data_new pcd 
group by 1
order by 2 desc
limit 20
;


-- графік 3
select
    cwe_id,
    count (*) as vulnerabilities_count
from pa_cve_data_new pcd 
group by 1
order by 2 desc
;