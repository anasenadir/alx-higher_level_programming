-- Count rows with id 89
-- cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
SELECT COUNT(1) from first_table WHERE id=89;
